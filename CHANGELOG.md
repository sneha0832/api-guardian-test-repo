# Payment API Changelog

## Version 2.0.0

### Breaking Changes

The `PaymentClient.old_charge()` method has been deprecated.

Applications must migrate to `PaymentClient.new_charge()`.

### Migration Guide

Before:
`client.old_charge(amount)`

After:
`client.new_charge(amount)`

The new method accepts the same arguments.
