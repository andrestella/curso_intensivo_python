from restaurant2 import Restaurant

restaurant = Restaurant('stella', 'italiana')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n")

restaurant2 = Restaurant('henri', 'americana')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('nádia', 'brasileira')
restaurant3.describe_restaurant()
restaurant4 = Restaurant('maria', 'paulista')
restaurant4.describe_restaurant()