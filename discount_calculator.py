def calculate_discount(price, discount_percent):
    """
    Calculates final price after applying discount if the discount is 20% or higher.

    Args:
        price (float): Original price of the item.
        discount_percent (float): Discount percentage to apply.

    Returns:
        float: Final price after discount
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price
    

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))


# Calculate and display the result
final_price = calculate_discount(original_price, discount)
if discount >= 20:
    print(f"Final price after {discount}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price: ${original_price:.2f}")