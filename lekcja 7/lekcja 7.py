def dzielenie(a, b):
    # assert b != 0, "Dzielnik nie może być zerem"
    return a * b

print(dzielenie(2, 3))
print(dzielenie(2, 5))
assert dzielenie(2, 4) == 0.5, "Błąd dzielenia"
