from data.find import find


results = find(
    search_text = "malmö", 
    sort_type = "price", 
    sort_direction = "ascending"
)

for r in results:
    print(r.price)