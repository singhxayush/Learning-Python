basket = [2, 1, 5, 3, 7, 2, 7]

print(basket.index(3))
print(basket.index(2)) # for multiple occuring, it gives the index of 1st occurance
# print(basket.index(200)) #for non occuring it throws an error

# int(element to be found, start range, end range) -> start : 0, end : end of list by default

# to check if an element is present in container or not before checking it
print(100 in basket)
print(1 in basket)

print(basket.count(10))
print(basket.count(2))

# print(basket.sort()) # will obvio return None

print(basket)

