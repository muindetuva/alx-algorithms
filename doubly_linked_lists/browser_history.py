#!/usr/bin/python3
"""Browser history implemented with a doubly linked list."""


class DoublyNode:
    """Store one URL and links to the adjacent history entries."""

    def __init__(self, url):
        """Create a history node that is not linked yet."""
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    """Support constant-time browser back, forward, and visit actions."""

    def __init__(self):
        """Create an empty browser history."""
        self.head = None
        self.tail = None
        self.current = None

    def visit(self, url):
        """Visit url and discard every page ahead of the current page."""
        new_page = DoublyNode(url)

        if self.current is None:
            self.head = new_page
            self.tail = new_page
            self.current = new_page
            return self.current.url

        forward_history = self.current.next
        if forward_history is not None:
            forward_history.prev = None

        self.current.next = new_page
        new_page.prev = self.current
        self.current = new_page
        self.tail = new_page
        return self.current.url

    def back(self):
        """Move back one page when an older page exists."""
        if self.current is not None and self.current.prev is not None:
            self.current = self.current.prev
        return self.get_current()

    def forward(self):
        """Move forward one page when a newer page exists."""
        if self.current is not None and self.current.next is not None:
            self.current = self.current.next
        return self.get_current()

    def get_current(self):
        """Return the current URL, or None when no page has been visited."""
        if self.current is None:
            return None
        return self.current.url

    def get_history(self):
        """Return every active history entry and mark the current page."""
        history = []
        page = self.head

        while page is not None:
            marker = " *" if page is self.current else ""
            history.append(f"{page.url}{marker}")
            page = page.next

        return history


if __name__ == "__main__":
    browser = BrowserHistory()
    browser.visit("google.com")
    browser.visit("youtube.com")
    browser.visit("github.com")
    browser.back()
    browser.back()
    browser.forward()
    browser.visit("twitter.com")
    browser.forward()
    browser.back()
    print("Current:", browser.get_current())
    print("History:", browser.get_history())
