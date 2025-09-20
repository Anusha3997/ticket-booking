"""
ticket_booking
A small, testable ticket-booking system to demonstrate Python OOP.
Public API exposes the main domain models and services.
"""

from .models import Seat, Show, Ticket  # domain entities
from .services import BookingService     # application/service layer
from .storage import Storage             # abstraction for persistence (JSON/SQLite etc.)

__all__ = [
    "Seat",
    "Show",
    "Ticket",
    "BookingService",
    "Storage",
]

# Semantic version for your package
__version__ = "0.1.0"

