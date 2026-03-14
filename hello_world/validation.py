import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def validate_row(row, seen_ids):

    errors = []

    order_id = row.get("order_id")
    price = row.get("price")
    quantity = row.get("quantity")
    customer_id = row.get("customer_id")
    product_id = row.get("product_id")
    order_timestamp = row.get("order_timestamp")

    # -------------------------
    # Validate order_id
    # -------------------------

    if not order_id:
        errors.append("Missing Order ID")

    elif order_id in seen_ids:
        errors.append("Duplicate Order ID")

    else:
        seen_ids.add(order_id)

    # -------------------------
    # Validate customer_id
    # -------------------------

    if not customer_id:
        errors.append("Missing Customer ID")

    # -------------------------
    # Validate product_id
    # -------------------------

    if not product_id:
        errors.append("Missing Product ID")

    # -------------------------
    # Validate price
    # -------------------------

    try:
        price_val = float(price)

        if price_val <= 0:
            errors.append("Invalid Price")

    except (ValueError, TypeError):
        errors.append("Price Not Numeric")

    # -------------------------
    # Validate quantity
    # -------------------------

    try:
        quantity_val = int(quantity)

        if quantity_val <= 0:
            errors.append("Invalid Quantity")

    except (ValueError, TypeError):
        errors.append("Quantity Not Numeric")

    # -------------------------
    # Validate timestamp
    # -------------------------

    try:
        datetime.strptime(order_timestamp, "%d-%m-%Y %H:%M")

    except Exception:
        errors.append("Invalid Order Timestamp")

    # -------------------------
    # Log validation errors
    # -------------------------

    if errors:
        logger.debug(f"Validation errors for row {row}: {errors}")

    return errors