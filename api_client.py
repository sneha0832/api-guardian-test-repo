
# ============================================================
# API Guardian - Test Repository
# File: api_client.py
#
# Purpose:
#   Simulate an application using outdated third-party
#   API methods so API Guardian can detect and fix them.
# ============================================================


class PaymentClient:
    """Simulated third-party payment API."""

    def old_charge(self, amount):
        return f"Legacy charge: ${amount}"

    def new_charge(self, amount):
        return f"Updated charge: ${amount}"


client = PaymentClient()

# Deprecated API usage: API Guardian should replace this.
result = client.old_charge(100)

print(result)
