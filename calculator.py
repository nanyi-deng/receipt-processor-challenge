import math

def calculate_points(receipt: dict) -> int:
    points = 0

    #if the character is either alphabetical or number, increment the points. 
    retailer = receipt.get("retailer", "")
    for ch in retailer:
        if ch.isalnum():
            points += 1

    # convert the total to float.
    total_str = receipt.get("total", "0")
    total_val = float(total_str)

    # check if the total_val (float), is integer or not. if so, add 50 to the point
    if total_val.is_integer():
        points += 50

    # check is muitple of 0.25 via checking the remainder of total_val * 100 and % 25 
    if (round(total_val * 100) % 25) == 0:
        points += 25

    # calcualate the number of items via length of the items array, every 2 items will get 5 points 
    # but the remainder should not be counted, so we should floor the number 
    items = receipt.get("items", [])
    num_items = len(items)
    points += 5 * (num_items // 2)

    # check each product's product description length, if the length >0 and is multiply of 3 
    # the price of the product should be times 0.2, and ceilled.  
    # the price will be added to the point
    for item in items:
        desc = item.get("shortDescription", "").strip()
        price_str = item.get("price", "0")
        price_val = float(price_str)

        if len(desc) > 0 and (len(desc) % 3 == 0):
            points += math.ceil(price_val * 0.2)



    #get the date of the purchase date, if it is divided by 2 with remainder as 1, add 6 to the points
    purchase_date = receipt.get("purchaseDate", "")
    day = int(purchase_date.split("-")[2])  
    if day % 2 == 1:  
        points += 6

    
    purchase_time = receipt.get("purchaseTime", "")
    #split the purchase time to hour and minutes 
    hour, minute = purchase_time.split(":")
    hour = int(hour)
    #if the hour is between 14-16 then point should add 10 
    if 14 <= hour < 16:
        points += 10

    return points
