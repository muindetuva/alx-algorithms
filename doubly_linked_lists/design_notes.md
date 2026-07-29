# Design Notes — AI Lab 3

## My Design — Before AI

### Data structure choice

I will use a doubly linked list.

This feature needs to remember pages in order, move backward, move forward, and remove everything after the current page when a new page is visited. A doubly linked list fits this because each page can point to the page before it and the page after it. That makes `back()` and `forward()` simple pointer moves instead of searching through the whole history.

The current page is the most important pointer because every operation depends on where the user is in the history.

### How the structure maps to the feature

- What does each node represent?

Each node represents one visited page. It stores the URL plus two pointers: `prev` for the previous page and `next` for the next page.

- What does `head` represent in the context of this feature?

`head` represents the oldest page in the browser history. If the user keeps pressing back, they cannot move before `head`.

- What does `tail` represent?

`tail` represents the newest page in the active browser history. If the user keeps pressing forward, they cannot move after `tail`.

- Where does the "current page" pointer sit?

The `current` pointer sits on whichever page the browser is currently showing. It may be at the `head`, at the `tail`, or somewhere in the middle after the user has gone back.

### The tricky part: clearing forward history

When a user visits a new page after going back, all forward history must disappear.

With a doubly linked list, this means the old `current.next` chain is no longer part of the active history. The pointer update is:

```python
current.next = new_node
new_node.prev = current
tail = new_node
current = new_node
```

Setting `current.next` to the new node disconnects the previous forward history. Updating `tail` to the new node makes the new page the most recent page.

If there is no current page yet, the first visited page becomes `head`, `tail`, and `current`.

### Operations and their expected complexity

| Operation | Expected complexity | Reasoning |
|---|---|---|
| visit(url) | O(1) | Create one node, attach it after `current`, clear forward history by replacing `current.next`, then update `tail` and `current`. |
| back() | O(1) | Move `current` to `current.prev` if it exists. |
| forward() | O(1) | Move `current` to `current.next` if it exists. |
| get_current() | O(1) | Return the URL stored at the `current` node. |

### Why not a Python list?

This feature could be built with a Python list and an integer index for the current page. The list would store the URLs in order, and `back()` or `forward()` would move the index.

The trade-off is that clearing forward history would require slicing the list after the current index before appending the new URL. That is still understandable, but it can copy or remove multiple items depending on the implementation. A doubly linked list models browser history more directly because visiting a new page can disconnect the old forward chain with pointer updates.

For this lab, I would choose the doubly linked list because the goal is to practise bidirectional links and pointer updates.

## Code Review — Before Running

### What looks correct

- `visit` handles the empty-history case by setting `head`, `tail`, and
  `current` to the same node.
- Each new node receives a backward link, and the former current node receives
  the matching forward link.
- `back` and `forward` check for an adjacent node before moving `current`, so
  attempts to move beyond either end leave the history unchanged.
- A visit after moving backward replaces `current.next` and moves `tail` to
  the new node, so abandoned forward pages are unreachable from the active
  list.

### What looks suspicious or unclear

- The abandoned forward chain must not retain a backward reference into the
  active history; the first detached node's `prev` link needs to be cleared.
- `tail` and `current` must always point to the new page after a visit from the
  middle of the history.
- `get_history` must compare node identity, not just URL text, because the same
  URL may be visited more than once.

### Edge cases to test

- Calling navigation methods before visiting any page.
- Moving backward at the oldest page and forward at the newest page.
- Navigating a one-page history.
- Clearing one or several forward entries with a new visit.
- Appending and navigating after forward history has been cleared.
- Marking the correct node when `get_history` traverses from head to tail.

## Design Reasoning — After AI Collaboration

### Did the AI recommend the same structure I did?

Yes. It compared a Python list, two stacks, and a doubly linked list before
recommending the DLL. Its recommendation matched my design because a current
node can move through `prev` and `next` links without searching or shifting
entries.

### What the AI got right in its design reasoning

It correctly identified that order matters, backward and forward movement
must both be fast, and a separate `current` reference is essential. It also
recognized that `head` and `tail` describe the active history boundaries and
that every core navigation operation can be constant time.

### What the AI missed or glossed over

The first explanation treated clearing forward history as only assigning a
new value to `current.next`. A complete trace also needs to state that the
first abandoned node's `prev` link is cleared, the new node points back to the
former current node, and both `current` and `tail` move to the new node.

### The key design insight

The `current` node is the navigation cursor. Visiting from the middle cuts its
forward link and attaches a new tail, so an entire obsolete forward chain is
discarded without traversing it.

### Complexity summary

| Operation | Complexity | Why |
|---|---|---|
| `visit(url)` | O(1) | It changes a fixed number of node references. |
| `back()` | O(1) | It follows one `prev` reference. |
| `forward()` | O(1) | It follows one `next` reference. |
| `get_current()` | O(1) | It reads the current node directly. |

### Why a Python list would have been worse

A list plus an index can make `back`, `forward`, and `get_current` constant
time. However, visiting from the middle requires deleting or slicing all
entries after the index, which takes O(k) time for k discarded pages. The DLL
performs that logical removal with a constant number of pointer updates.

## Reflection

Using AI during design produced a more useful trade-off discussion than using
it only to generate or repair code in Labs 1 and 2. It was especially useful
for challenging the initial choice with a list-based alternative, although
the exact pointer order still required careful human review.

`visit` is harder than `back` or `forward` because it changes the structure,
not merely the cursor. It must detach an arbitrary forward chain, attach a new
node in both directions, and synchronize `current` and `tail`; overlooking any
one of those references can leave stale history reachable.

Use a DLL when movement in both directions and constant-time insertion or
branch replacement are central requirements. Use an SLL when traversal is
mainly forward and the extra backward pointer would add needless overhead.
Use a Python list when indexed access, simplicity, and cache-friendly storage
matter more than frequent structural edits in the middle.
