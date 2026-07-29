#!/usr/bin/python3
"""Tests for the customer support ticket system."""

from ticket_system import TicketSystem


def test_severity_ordering():
    """Higher severity tickets are processed before lower severity."""
    system = TicketSystem()
    system.submit_ticket("T1", "Login broken", severity=3)
    system.submit_ticket("T2", "Data loss", severity=1)
    system.submit_ticket("T3", "Slow response", severity=4)
    system.submit_ticket("T4", "Payment failing", severity=2)

    order = []
    while not system.is_empty():
        ticket, _ = system.process_next()
        order.append(ticket)

    assert order == ["T2", "T4", "T1", "T3"], (
        f"Expected ['T2', 'T4', 'T1', 'T3'], got {order}"
    )
    print("severity ordering: PASSED")


def test_arrival_order_within_same_severity():
    """Earlier tickets are processed first within the same severity."""
    system = TicketSystem()
    system.submit_ticket("First", "Issue A", severity=2)
    system.submit_ticket("Second", "Issue B", severity=2)
    system.submit_ticket("Third", "Issue C", severity=2)

    order = []
    while not system.is_empty():
        ticket, _ = system.process_next()
        order.append(ticket)

    assert order == ["First", "Second", "Third"], (
        f"Expected FIFO within same severity, got {order}"
    )
    print("arrival order within same severity: PASSED")


def test_scenario_from_spec():
    """Reproduce the exact example: B, D, C, A."""
    system = TicketSystem()
    system.submit_ticket("A", "Ticket A", severity=3)
    system.submit_ticket("B", "Ticket B", severity=1)
    system.submit_ticket("C", "Ticket C", severity=2)
    system.submit_ticket("D", "Ticket D", severity=1)

    order = []
    while not system.is_empty():
        ticket, _ = system.process_next()
        order.append(ticket)

    assert order == ["B", "D", "C", "A"], (
        f"Expected ['B', 'D', 'C', 'A'], got {order}"
    )
    print("scenario from spec: PASSED")


def test_process_next_on_empty():
    """Processing an empty queue raises an error."""
    system = TicketSystem()
    try:
        system.process_next()
    except IndexError:
        print("process_next on empty: PASSED")
    else:
        raise AssertionError("Expected IndexError")


def test_peek_next_does_not_remove():
    """Peeking returns the next ticket without removing it."""
    system = TicketSystem()
    system.submit_ticket("T1", "Critical issue", severity=1)
    system.submit_ticket("T2", "Low issue", severity=4)

    peeked, _ = system.peek_next()
    assert peeked == "T1", f"Expected T1, got {peeked}"
    assert system.tickets_waiting() == 2, (
        f"Expected 2 tickets, got {system.tickets_waiting()}"
    )
    print("peek_next does not remove: PASSED")


def test_tickets_waiting_count():
    """The waiting count changes after submissions and processing."""
    system = TicketSystem()
    assert system.tickets_waiting() == 0
    system.submit_ticket("T1", "Issue", severity=2)
    assert system.tickets_waiting() == 1
    system.submit_ticket("T2", "Issue", severity=3)
    assert system.tickets_waiting() == 2
    system.process_next()
    assert system.tickets_waiting() == 1
    print("tickets_waiting count: PASSED")


def test_single_ticket():
    """The system processes exactly one ticket correctly."""
    system = TicketSystem()
    system.submit_ticket("Only", "Single issue", severity=2)
    assert system.tickets_waiting() == 1
    ticket, severity = system.process_next()
    assert ticket == "Only"
    assert severity == 2
    assert system.is_empty()
    print("single ticket: PASSED")


def test_get_all_waiting():
    """List processing order without removing any queued tickets."""
    system = TicketSystem()
    system.submit_ticket("A", "Medium", severity=3)
    system.submit_ticket("B", "Critical first", severity=1)
    system.submit_ticket("C", "High", severity=2)
    system.submit_ticket("D", "Critical second", severity=1)

    assert system.get_all_waiting() == ["B", "D", "C", "A"]
    assert system.tickets_waiting() == 4
    assert system.peek_next() == ("B", 1)
    print("get_all_waiting does not remove: PASSED")


def test_invalid_severity():
    """Reject severity values outside the documented range."""
    system = TicketSystem()
    try:
        system.submit_ticket("Bad", "Invalid", severity=5)
    except ValueError:
        assert system.is_empty()
        print("invalid severity: PASSED")
    else:
        raise AssertionError("Expected ValueError")


if __name__ == "__main__":
    print("Running TicketSystem tests...\n")
    test_severity_ordering()
    test_arrival_order_within_same_severity()
    test_scenario_from_spec()
    test_process_next_on_empty()
    test_peek_next_does_not_remove()
    test_tickets_waiting_count()
    test_single_ticket()
    test_get_all_waiting()
    test_invalid_severity()
    print("\nAll tests complete.")
