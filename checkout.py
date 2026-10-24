
# ============================================================
# API Guardian - Test Checkout Module
# File: checkout.py
#
# Purpose:
#   Provide a second outdated API usage for testing
#   multi-file migration functionality.
# ============================================================

from api_client import PaymentClient


def checkout(amount):
    """Process a simulated customer payment."""

    client = PaymentClient()

    # Deprecated API usage.
    return client.old_charge(amount)


if __name__ == "__main__":
    print(checkout(50))
