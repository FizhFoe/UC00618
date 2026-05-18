# Create the set
# Print the set
# Add "yellow"
# Remove "green"
# Print the number of items
colors = {"blue", "green", "brown", "orange", "purple", "black"}
print(colors)

colors.add("yellow")
print(colors)
colors.remove("green")

print(f"Nº Items: ", len(colors))
print("----------")
# Create the dictionary
# Print the model
# Add a color key
# Remove the brand key
# Print the dictionary
decor = {
    "name": "TV Stand",
    "brand": "IKEA",
    "material": "plywood"
}

print(decor["name"])
decor["color"] = "yellow"
del decor["brand"]
print(decor)

