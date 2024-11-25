"""

Author:  Daniela Zamorano-Martinez
Date written: 11/18/24
Assignment:   Module04 Programming Assignment part2
Short Desc:   Displays the top 3 most expensive item from the list
"""
def main():
    #test data
    item_price = {
        'Lettuce': 2.00,
        'Cereal' : 4.95,
        'Milk': 2.50,
        'Banana': .10,
        'Eggs': 3.00,
        '2-liter soda': 2.75,
        'Vanilla Extract': 4.95,
        'Chocolate covered Strawberries': 2.50,

    }

    sort_item = sorted(item_price.items(), key=lambda x: x[1], reverse = True)[:3]

    for item in sort_item:
        print(f"{item[0]} {item[1]:.2f}")

if __name__ == "__main__":
    main()
    