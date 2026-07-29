#!/usr/bin/python3
"""Tests for the doubly linked browser history implementation."""

from browser_history import BrowserHistory


def test_basic_navigation():
    """Move backward and forward through three pages."""
    browser = BrowserHistory()
    browser.visit("google.com")
    browser.visit("youtube.com")
    browser.visit("github.com")
    assert browser.get_current() == "github.com"
    browser.back()
    assert browser.get_current() == "youtube.com"
    browser.back()
    assert browser.get_current() == "google.com"
    browser.forward()
    assert browser.get_current() == "youtube.com"
    print("basic navigation: PASSED")


def test_forward_history_cleared_on_visit():
    """A new visit after back navigation must discard newer pages."""
    browser = BrowserHistory()
    browser.visit("google.com")
    browser.visit("youtube.com")
    browser.visit("github.com")
    browser.back()
    browser.visit("twitter.com")
    browser.forward()
    assert browser.get_current() == "twitter.com", (
        f"Expected twitter.com, got {browser.get_current()}"
    )
    print("forward history cleared on visit: PASSED")


def test_back_at_oldest_page():
    """Back at the oldest page should leave the current page unchanged."""
    browser = BrowserHistory()
    browser.visit("google.com")
    browser.back()
    assert browser.get_current() == "google.com"
    print("back at oldest page: PASSED")


def test_forward_at_newest_page():
    """Forward at the newest page should leave the current page unchanged."""
    browser = BrowserHistory()
    browser.visit("google.com")
    browser.visit("youtube.com")
    browser.forward()
    assert browser.get_current() == "youtube.com"
    print("forward at newest page: PASSED")


def test_single_page_history():
    """A one-page history should remain stable in both directions."""
    browser = BrowserHistory()
    browser.visit("google.com")
    browser.back()
    assert browser.get_current() == "google.com"
    browser.forward()
    assert browser.get_current() == "google.com"
    print("single page history: PASSED")


def test_visit_after_back_clears_forward():
    """Discard multiple forward entries after backing up and visiting."""
    browser = BrowserHistory()
    browser.visit("a.com")
    browser.visit("b.com")
    browser.visit("c.com")
    browser.visit("d.com")
    browser.back()
    browser.back()
    browser.visit("x.com")
    browser.forward()
    assert browser.get_current() == "x.com", (
        f"Expected x.com, got {browser.get_current()}"
    )
    browser.back()
    assert browser.get_current() == "b.com", (
        f"Expected b.com, got {browser.get_current()}"
    )
    print("visit after back clears forward: PASSED")


def test_empty_history():
    """Navigation on an empty history should return None safely."""
    browser = BrowserHistory()
    assert browser.get_current() is None
    assert browser.back() is None
    assert browser.forward() is None
    assert browser.get_history() == []
    print("empty history: PASSED")


def test_get_history():
    """Return active history in order and identify the current page."""
    browser = BrowserHistory()
    browser.visit("google.com")
    browser.visit("youtube.com")
    browser.visit("github.com")
    browser.back()
    assert browser.get_history() == [
        "google.com",
        "youtube.com *",
        "github.com",
    ]
    browser.visit("twitter.com")
    assert browser.get_history() == [
        "google.com",
        "youtube.com",
        "twitter.com *",
    ]
    print("get history: PASSED")


if __name__ == "__main__":
    print("Running BrowserHistory tests...\n")
    test_basic_navigation()
    test_forward_history_cleared_on_visit()
    test_back_at_oldest_page()
    test_forward_at_newest_page()
    test_single_page_history()
    test_visit_after_back_clears_forward()
    test_empty_history()
    test_get_history()
    print("\nAll tests complete.")
