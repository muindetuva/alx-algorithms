#!/usr/bin/python3
"""A stable priority queue for customer support tickets."""

import heapq
from dataclasses import dataclass


@dataclass(frozen=True)
class Ticket:
    """Represent the information stored for one support request."""

    ticket_id: str
    description: str
    severity: int
    arrival_order: int


class TicketSystem:
    """Process tickets by severity, then by their submission order."""

    VALID_SEVERITIES = {1, 2, 3, 4}

    def __init__(self):
        """Create an empty ticket heap and initialize its tiebreaker."""
        self._tickets = []
        self._next_arrival = 0

    def submit_ticket(self, ticket_id, description, severity):
        """Add a validated ticket while preserving its arrival order."""
        if severity not in self.VALID_SEVERITIES:
            raise ValueError("severity must be an integer from 1 to 4")

        ticket = Ticket(
            ticket_id=ticket_id,
            description=description,
            severity=severity,
            arrival_order=self._next_arrival,
        )
        heapq.heappush(
            self._tickets,
            (ticket.severity, ticket.arrival_order, ticket),
        )
        self._next_arrival += 1
        return ticket

    def process_next(self):
        """Remove and return the next ticket ID and severity."""
        if self.is_empty():
            raise IndexError("no tickets are waiting")

        _, _, ticket = heapq.heappop(self._tickets)
        return ticket.ticket_id, ticket.severity

    def peek_next(self):
        """Return the next ticket ID and severity without removing it."""
        if self.is_empty():
            raise IndexError("no tickets are waiting")

        ticket = self._tickets[0][2]
        return ticket.ticket_id, ticket.severity

    def tickets_waiting(self):
        """Return the number of tickets currently stored in the heap."""
        return len(self._tickets)

    def is_empty(self):
        """Return whether there are no tickets waiting."""
        return not self._tickets

    def get_all_waiting(self):
        """Return ticket IDs in processing order without changing the heap."""
        return [entry[2].ticket_id for entry in sorted(self._tickets)]


if __name__ == "__main__":
    system = TicketSystem()
    system.submit_ticket("A", "Ticket A", severity=3)
    system.submit_ticket("B", "Ticket B", severity=1)
    system.submit_ticket("C", "Ticket C", severity=2)
    system.submit_ticket("D", "Ticket D", severity=1)

    processing_order = []
    while not system.is_empty():
        ticket_id, _ = system.process_next()
        processing_order.append(ticket_id)

    print("Processing order:", " → ".join(processing_order))
