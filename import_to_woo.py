import csv

# List of Vendors who have restrictions for selling online
#   Brome
#   Chippy Chipmunk
#   Aspects
#   Cork Pop
#   GOVINO
#   Greenway
#   Music of the Spheres
#   WineSkin



# For each product, this function will map the Goldcrest-assigned categories 
# to categories that Chirp is using in Woo. This should include subcategories.
def getCategories(input_row):    

    # Get the categories (max of 4) from the input product
    cat1 = int(input_row[24]) if input_row[24] else input_row[24]
    cat2 = int(input_row[25]) if input_row[25] else input_row[25]
    cat3 = int(input_row[26]) if input_row[26] else input_row[26]
    cat4 = int(input_row[27]) if input_row[27] else input_row[27]

    input_cats = [ cat1, cat2, cat3, cat4 ]

    output_categories = []

    # We need to add subcategories for each category.
    # Bird Feeders
        # Squirrel Proof Feeders - 255
        # Caged Bird Feeders
        # Nyjer Seed Bird Feeders - 199
        # Duncraft Brand Feeders
        # Hopper Bird Feeders
        # Tube Bird Feeders
        # Window Bird Feeders - 198
        # Suet and Block Feeders - 182
        # Hummingbird Feeders - 147
        # Oriole Bird Feeders - 162
        # Platform Feeders
        # Fruit & Nut Feeders - 140, 201
        # Bluebird Feeders
        # Decorative Bird Feeders
        # Pole-Mount Bird Feeders
    # Bird Seed & Foods
        # No-Waste! No-Mess Seeds
        # Bird Seed Blends & Mixes - 242
        # Suet Cakes, Balls & Plugs - 176
        # Bird Seed Blocks, Cakes & Bars
        # Mealworms & Insect Foods - 249
        # Wildlife, Corn & Nuggets
        # Fruits, Nuts & Jelly - 241
        # Hummingbird & Oriole Nectar - 163, 148
        # Hot Pepper Foods
        # Squirrel Foods
        # Seed Storage & Scoops
    # Bird Baths
        # Pedestal Bird Baths
        # Solar Powered Bird Baths - 230
        # Water Misters & Drippers - 134
        # Hanging Bird Baths
        # Decorative Bird Baths
        # Ground Bird Baths
        # Deck Mounted Bird Baths
        # Heated Baths & Heaters - 254
        # Fountains & Water Wigglers - 139
    # Bird Houses
        # Bluebird Houses
        # BestBasic Houses
        # Songbird & Roosting Boxes
        # Window View
        # Decorative Houses
        # Hummingbird Houses
        # Purple Martin Houses
        # Chickadee & Wren Houses
        # Bird House Accessories
        # Guards & Poles
        # Nesting Materials - 159
        # Bat Houses
        # Nest Boxes - 186
    # Accessories 
        # Brackets, Hangers & Posts
        # Squirrel Baffles & Guards - 169
        # Cleaning Supplies - 229, 250, 251, 252
        # Window Strike Solutions
        # Seed Trays for Tube Feeders - 175
        # Hummingbird Accessories
        # Seed Storage & Scoops - 177
        # Mounting Hardware - 196
        # Ground Mounts
        # Deck Mounts
        # Poles
        # Feeder Mounts
        # Arms/Brackets
        # Hooks and Hangers
        # Accessory items
        # Water Feature Accessories - 195
    # Bird Watching
        # Guides & Books
        # Binoculars
        # Spotting Scopes
        # Digiscoping
    # Critters 
        # Squirrel Feeders & Houses
        # Squirrel Foods
        # Squirrel Baffles & Guards - 169
        # Squirrel Deterrents
        # Poultry Supplies
        # Butterflies & Insects - 118
        # Bats - 103
    # Gifts
        # Garden Decor - 436, 142
        # Nature Gifts
        # Outdoor Pest Controls
        # Wind and Weather
        # Guides - Books - DVD's
        # Apparel - 410
        # Games - 141
        # Calendars - 120
        # CDs & DVDs - 125
        # Clocks - 128
        # Door Mats & Door Stops - 133
        # Flags - 136
        # Posters - 168
        # Puzzles - 171
        # Signs - 178


    categories = {
        "accessories": {
            "keys": [100, 106, 108, 117, 134, 135, 136, 139, 149, 153, 159, 169, 173, 177, 185, 193, 194, 195, 196, 229, 250, 253, 257, 258, 436],
            "subcategories": {
                "baffles": {
                    "keys": [169],
                    "chirp subcategory": "Squirrel Baffles & Guards"
                },
                "cleaning": {
                    "keys": [229, 250, 251, 252],
                    "chirp subcategory": "Cleaning Supplies"
                },
                "trays": {
                    "keys": [175],
                    "chirp subcategory": "Seed Trays for Tube Feeders"
                },
                "storage & scoops": {
                    "keys": [177],
                    "chirp subcategory": "Seed Storage & Scoops"
                },
                "mounting hardware": {
                    "keys": [196],
                    "chirp subcategory": "Mounting Hardware"
                },
                "water feature": {
                    "keys": [195],
                    "chirp subcategory": "Bath & Fountain Accessories"
                }
            },
            "chirp category": "Accessories"
        },
        "bird baths": {
            "keys": [107, 139, 230, 254],
            "subcategories": {
                "solar": {
                    "keys": [230],
                    "chirp subcategory": "Solar Powered Bird Baths"
                },
                "misters": {
                    "keys": [134],
                    "chirp subcategory": "Water Misters & Drippers"
                },
                "heated": {
                    "keys": [254],
                    "chirp subcategory": "Heated Bird Baths"
                },
                "fountains": {
                    "keys": [139],
                    "chirp subcategory": "Fountains & Water Wigglers"
                }
            },
            "chirp category": "Bird Baths"
        },
        "bird feeders": {
            "keys": [110, 140, 147, 157, 175, 182, 198, 199, 200],
            "subcategories": {
                "squirrel proof": {
                    "keys": [255],
                    "chirp subcategory": "Squirrel Proof Feeders"
                },
                "nyjer thistle": {
                    "keys": [199],
                    "chirp subcategory": "Nyjer Thistle Feeders" 
                },
                "window": {
                    "keys": [198],
                    "chirp subcategory": "Window Feeders"
                },
                "suet & block": {
                    "keys": [182],
                    "chirp subcategory": "Suet & Block Feeders"
                },
                "hummingbird": {
                    "keys": [147],
                    "chirp subcategory": "Hummingbird Feeders"
                },
                "oriole": {
                    "keys": [162],
                    "chirp subcategory": "Oriole Feeders"
                },
                "fruit & nut": {
                    "keys": [140, 201],
                    "chirp subcategory": "Fruit & Nut Feeders"
                }
            },
            "chirp category": "Bird Feeders"
        },
        "bird houses": {
            "keys": [113, 204, 221],
            "subcategories": {
                "nesting materials": {
                    "keys": [159],
                    "chirp subcategory": "Nesting Materials"
                },
                "nest box": {
                    "keys": [186],
                    "chirp subcategory": "Nest Boxes"
                }
            },
            "chirp category": "Bird Houses"
        },
        "bird seed": {
            "keys": [241, 242, 176, 148, 249],
            "subcategories": {
                "blend & mixes": {
                    "keys": [242],
                    "chirp subcategory": "Bird Seed Blend & Mixes"
                },
                "suet": {
                    "keys": [176],
                    "chirp subcategory": "Suet Cakes, Balls & Plugs"
                },
                "mealworms": {
                    "keys": [249],
                    "chirp subcategory": "Mealworms & Insect Foods"
                },
                "nuts": {
                    "keys": [241],
                    "chirp subcategory": "Fruits Nuts & Jelly"
                },
                "nectar": {
                    "keys": [163, 148],
                    "chirp subcategory": "Hummingbird & Oriole Nectar"
                }   
            },
            "chirp category": "Bird Seed & Foods"
        },
        "bird watching": {
            "keys": [161],
            "subcategories": {
                "binoculars": {
                    "keys": [],
                    "chirp subcategory": "Binoculars"
                }
            },
            "chirp category": "Bird Watching"
        },
        "books": {
            "keys": [115, 116],
            "subcategories": {
                "": {
                    "keys": [],
                    "chirp subcategory": ""
                }
            },
            "chirp category": "Books"
        },
        "critters": {
            "keys": [103, 181, 277],
            "subcategories": {
                "butterflies": {
                    "keys": [118],
                    "chirp subcategory": "Butterflies & Insects"
                },
                "bats": {
                    "keys": [103],
                    "chirp subcategory": "Bat"
                }
            },
            "chirp category": "Critters"
        },
        "gifts": {
            "keys": [120, 122, 125, 128, 130, 131, 133, 136, 137, 141, 142, 143, 144, 145, 150, 152, 155, 
            158, 160, 164, 166, 168, 171, 178, 181, 190, 202, 203, 207, 213, 245, 264, 412, 413],
            "subcategories": {
                "garden decor": {
                    "keys": [436, 142],
                    "chirp subcategory": "Garden Decor"
                },
                "apparel": {
                    "keys": [410],
                    "chirp subcategory": "Apparel"
                },
                "games": {
                    "keys": [141],
                    "chirp subcategory": "Games"
                },
                "calendars": {
                    "keys": [120],
                    "chirp subcategory": "Calendars"
                },
                "cds & dvds": {
                    "keys": [125],
                    "chirp subcategory": "CDs & DVDs"
                },
                "clocks": {
                    "keys": [128],
                    "chirp subcategory": "Clocks"
                },
                "door mats": {
                    "keys": [133],
                    "chirp subcategory": "Door Mats & Door Stops"
                },
                "flags": {
                    "keys": [136],
                    "chirp subcategory": "Flags"
                },
                "posters": {
                    "keys": [168],
                    "chirp subcategory": "Posters"
                },
                "puzzles": {
                    "keys": [171],
                    "chirp subcategory": "Puzzles"
                },
                "signs": {
                    "keys": [178],
                    "chirp subcategory": "Signs"
                },
            },
            "chirp category": "Gifts"
        }
    }


    for input_cat in input_cats:
        # Loop through the Categories dictionary
        for category_key in categories:
            category_dict = categories[category_key]
            # For each category, loop through it's subcategories
            for subcat_key in category_dict["subcategories"]:
                subcat_dict = category_dict["subcategories"][subcat_key]
                # For each subcategory, check if input_cat is in the list of keys
                if input_cat in subcat_dict["keys"]:
                    # The input category maps to this subcategory so append that subcat string to list
                    output_categories.append( category_dict["chirp category"] + " > " + subcat_dict["chirp subcategory"] )
                    # Also append the parent, root category to the list
                    output_categories.append( category_dict["chirp category"] )
            
            if input_cat in category_dict["keys"]:
                output_categories.append( category_dict["chirp category"])

    # Next we need to remove duplicate elements
    output_categories = list( set( output_categories ) )

    # Convert list to a string
    output_string = ", ".join(output_categories)

    return output_string

# Sets price to suggested as long as suggested price is higher than MAP
def getPrice(price, map):
    # Check if product has a MAP. If not, just use suggested price
    if not map:
        return price
    
    if float(price) > float(map):
        return price
    
    return map



input_file = open('input.csv', 'r')

input_reader = csv.reader(input_file, delimiter=',')

input_list = list(input_reader)

# Table of relavant input columns

# Input Column #    Input Column                Output #
# 15                Minimum Case QTY            3
# 0                 Manufacturers               4 
# 1                 Products ItemNo             5 
# 4                 Products UPC                6
# 2                 Products Name               7
# 3                 Descriptions                8 & 9
# y                 Dropshippable               11
# 5                 Products Weight             12  *convert to oz
# 24                Products Category 1         15
# 25                Products Category 2         15
# 26                Products Category 3         15
# 27                Products Category 4         15
# 14                Suggested_Retail_Price      17
# 13                Products Wholesale Price    18
# 12                Products Map Price          23
# 14                Chirp Retail Price          24
# 10                Actual_Item_Width           26
# 9                 Actual_Item_Height          27
# 11                Actual_Item_Depth           28
# 19                Products Image              29  *change to absolute URL using Manufacturer + Products Image


# Hard code the columns of the output - which are the same columns used for the Chirp spreadsheet
output_headers = ['line', 'qty_ordered', 'qty_available', 'vendor_minimum', 'vendor', 'sku/vendor_part_num', 'upc',
                    'name', 'full_detailed_product_description', 'short_summary/overview_product_description',
                    'where_sold', 'dropshipable', 'weight_each_oz', '', 'dimensions', 'product_category',
                    'relevant_product_keywords_or_tags', 'regular_retail_price', 'wholesale_price_each', 'shipping_cost_each',
                    'total_cost_each', 'multiplier', 'working _sales_price', 'map', 'chirp_retail_price', 'chirp_part_num',
                    'product_width_in', 'product_height_in', 'product_depth_in', 'image_urls']
# The list which rows/lists will be written to
output_list = []

# Next we need to go through each row in the input list and for each create a corresponding row for the output row
i = 0

for input_row in input_list:

    if i == 0:
        # add output_headers to output_list (as the first row)
        output_list.append(output_headers)
    else:
        # Initialize row with empty values - Only some of the elements in this list will be given actual values
        output_row = [""] * len(output_headers)

        # Note: not every field in the output file needs to have a value. For instance, line, Qty Ordered etc.
        # We'll do these in the order in which they appear in the output file i.e Vendor Minimum (3), Vendor (4) etc.

        # Vender Minimum
        output_row[3] = input_row[15]

        # Vendor
        output_row[4] = input_row[0]

        # SKU 
        output_row[5] = input_row[1]

        # UPC
        output_row[6] = input_row[4]

        # Name 
        output_row[7] = input_row[2]

        # Short & Full Description - Goldcrest only provides one description
        output_row[8] = input_row[3]
        output_row[9] = input_row[3]

        # Dropshippable 
        output_row[11] = 'y'

        # Weight - Convert from lbs to oz
        output_row[12] = float(input_row[5]) * 16

        # Category
        output_row[15] = getCategories(input_row)

        # Retail Price
        output_row[17] = getPrice(input_row[14], input_row[12])

        # Wholesale Price
        output_row[18] = input_row[13]

        # MAP Price
        output_row[23] = input_row[12]

        # Width
        output_row[26] = input_row[10]

        # Height
        output_row[27] = input_row[9]

        # Depth
        output_row[28] = input_row[11]

        # Image(s)
        image_url = "https://chirpforbirds.com/Product_Images/" + input_row[0] + "/" + input_row[19]
        output_row[29] = image_url.replace(',', '')

        #finally append this row to the output_list
        output_list.append(output_row)


    i += 1


with open('output.csv', 'w') as writeFile:
    writer = csv.writer( writeFile )
    writer.writerows( output_list )
