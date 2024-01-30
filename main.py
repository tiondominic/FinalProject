import json
from requests import get
print("Final Project\nBy: James Dominic P. Tion - CS1D\nFinds Prices for TF2 Items in the Steam Market\n")

class Items:
    def __init__(self, itemhash):
        self.itemhash = itemhash
    # API Limit of 20 requests per minute
    def itemget(self):
        if self.is_duplicate() != True:
            steam = get(f"https://steamcommunity.com/market/priceoverview/?country=PH&currency=12&appid=440&market_hash_name={self.itemhash}")
            self.itemprice(steam)
            # appid (gameid in steam), 440 = TF2, idea add change appid, currency, country, update prices, hashnames in steam market
            # currencies https://partner.steamgames.com/doc/store/pricing/currencies
    def itemprice(self, data):
        item = data.json()
        item["Item_hash"] = self.itemhash
        with open("pricedata.json", "a") as file:
            json.dump(item, file)
            file.write('\n')
        file.close()

    def is_duplicate(self):
        with open("pricedata.json", "r") as file:
            for line in file:
                existing_entry = json.loads(line)
                if existing_entry["Item_hash"] == self.itemhash:
                    print("Already exists")
                    return True
        return False


class selections:
    def Check_Price(self):
        with open("pricedata.json", "r") as file:
            for line in file:
                prices = json.loads(line)
                item_hash = prices["Item_hash"]
                low = prices["lowest_price"]
                median = prices["median_price"]
                print(format(f"item_name: {item_hash} {low}, median: {median}"), end="\n")
        print("")
        Select()

    def Add_Item(self):
        data = Items(input("Item name (Use Hash name): "))
        data.itemget()
        print("Added!\n")
        Select()

    def Exit(self):
        print("Ciao!")
        exit()


def Select():
    whatclass = selections()
    methods = dir(selections)
    counter = 1
    method_names = []
    for items in methods:
        if items.startswith('__'):
            print("", end="")
        else:
            method_names.append(items)
            print(f"{counter}. {items}")
            counter += 1

    choice = int(input("\nSelect: "))
    if 1 <= choice <= len(method_names):
        selected_method = getattr(whatclass, method_names[choice - 1])
        print("")
        selected_method()

    else:
        print("Invalid number!")


Select()

# https://steamcommunity.com/market/listings/440/Battle-Worn%20Robot%20Taunt%20Processor - Example item
