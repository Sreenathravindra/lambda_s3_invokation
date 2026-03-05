import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def validate_row(row, seen_ids):

    errors = []

    order_id = row.get("order_id")
    amount = row.get("amount")
    quantity = row.get("quantity")

    # Validate order_id
    if not order_id:
        errors.append("Missing Order ID")

    elif order_id in seen_ids:
        errors.append("Duplicate Order ID")

    else:
        seen_ids.add(order_id)

    # Validate amount
    try:
        amount_val = float(amount)

        if amount_val <= 0:
            errors.append("Invalid Amount")

    except (ValueError, TypeError):
        errors.append("Amount Not Numeric")

    # Validate quantity
    try:
        quantity_val = int(quantity)

        if quantity_val <= 0:
            errors.append("Invalid Quantity")

    except (ValueError, TypeError):
        errors.append("Quantity Not Numeric")

    if errors:
        logger.debug("Validation errors for row %s : %s", row, errors)

    return errors