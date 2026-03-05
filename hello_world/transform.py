def transform_row(row):

    # convert order_id to integer
    row["order_id"] = int(row["order_id"])

    # convert amount to float
    row["amount"] = float(row["amount"])

    # convert quantity to integer
    row["quantity"] = int(row["quantity"])

    # clean customer name
    row["customer_name"] = row["customer_name"].strip()

    # lowercase product name
    row["product"] = row["product"].lower()

    # clean city name
    row["city"] = row["city"].strip()

    return row