from decimal import Decimal


def calculate_total_weight(order):
    total_weight = Decimal("0")

    for item in order.items.select_related("product").all():
        total_weight += item.product.weight * item.quantity

    return total_weight
def product_fits_box(product, box):
    product_dimensions = sorted([
        product.length,
        product.width,
        product.height,
    ])

    box_dimensions = sorted([
        box.internal_length,
        box.internal_width,
        box.internal_height,
    ])

    return all(
        product_dimension <= box_dimension
        for product_dimension, box_dimension
        in zip(product_dimensions, box_dimensions)
    )
def get_suitable_boxes(order, boxes):
    total_weight = calculate_total_weight(order)

    suitable_boxes = []

    for box in boxes:
        if total_weight > box.max_weight:
            continue

        all_products_fit = all(
            product_fits_box(item.product, box)
            for item in order.items.select_related("product").all()
        )

        if all_products_fit:
            suitable_boxes.append(box)

    return suitable_boxes

def recommend_box(order, boxes):
    suitable_boxes = get_suitable_boxes(order, boxes)

    if not suitable_boxes:
        return None

    return min(suitable_boxes, key=lambda box: box.cost)