import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def validate_row(row, seen_ids):

    errors = []

    # Clean values (important!)
    order_id = (row.get("order_id") or "").strip()
    price = (row.get("price") or "").strip()
    quantity = (row.get("quantity") or "").strip()
    timestamp = (row.get("order_timestamp") or "").strip()

    # Validate order_id
    if not order_id:
        errors.append("Missing Order ID")

    elif order_id in seen_ids:
        errors.append("Duplicate Order ID")

    else:
        seen_ids.add(order_id)

    # Validate price
    try:
        price_val = float(price)

        if price_val <= 0:
            errors.append("Invalid Price")

    except (ValueError, TypeError):
        errors.append("Price Not Numeric")

    # Validate quantity
    try:
        quantity_val = int(quantity)

        if quantity_val <= 0:
            errors.append("Invalid Quantity")

    except (ValueError, TypeError):
        errors.append("Quantity Not Numeric")

    # Validate timestamp
    try:
        datetime.strptime(timestamp, "%d-%m-%Y %H:%M")

    except Exception:
        errors.append("Invalid Timestamp")

    if errors:
        logger.debug("Validation errors for row %s : %s", row, errors)

    return errors