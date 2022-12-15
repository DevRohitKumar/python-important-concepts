# We used lists, tuples, lambda and map() to create a simple currency
# converter for various stores🏪

store_dollars = [
    ("shirt", 16.00),
    ("pants", 18.25),
    ("socks", 4.78),
    ("jacket", 26.12),
    ("shoes", 31.62),
    ("thermals", 13.45)]

to_euros = lambda rate: (rate[0], rate[1]*0.94)
to_inr = lambda rate: (rate[0], rate[1]*82.46)

store_euros = list(map(to_euros, store_dollars))
store_inr = list(map(to_inr, store_dollars))
                     
for i in store_euros:
    print(i)
print("******")
    
for j in store_inr:
    print(j)