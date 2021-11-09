def shopping_list(budget, **kwargs):
    bought_products = 0
    output = ''
    if budget < 100:
        return 'You do not have enough budget.'
    for product, price_qty in kwargs.items():
        total_price = price_qty[0] * price_qty[1]
        if total_price <= budget:
            output += f'You bought {product} for {total_price:.2f} leva.\n'
            bought_products += 1
            budget -= total_price
            if bought_products == 5:
                return output
    return output

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))