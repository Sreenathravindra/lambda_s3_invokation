import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def validate_row(row, seen_ids):
    """
    Validate a single CSV row
    """
    errors = []

    order_id = row.get("order_id")
    amount = row.get("amount")

    # Validate order_id
    if not order_id:
        errors.append("Missing Order ID")
    elif order_id in seen_ids:
        errors.append("Duplicate Order ID")
    else:
        seen_ids.add(order_id)

    # Validate amount
    try:
        amount_value = float(amount)

        if amount_value <= 0:
            errors.append("Invalid Amount")
        else:
            row["amount"] = amount_value

    except (ValueError, TypeError):
        errors.append("Amount Not Numeric")

    if errors:
        logger.debug("Validation failed for row %s: %s", row, errors)

    return errors