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
