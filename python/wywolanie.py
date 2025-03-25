from zadanie_1 import D, N, P, Z
from zadanie_2 import most_contracts
from zadanie_3 import majority_children
from zadanie_4 import parent_initials
from zadanie_5 import YYY

print("» zadanie 1:")
print("   ", f"D: {len(D)}\n"
      "   ", f"N: {len(N)}\n"
      "   ", f"P: {len(P)}\n"
      "   ", f"Z: {len(Z)}\n")

print("» zadanie 2:")
print("   ", f"{most_contracts[0][0]} {most_contracts[0][1]} ({len(most_contracts[1])})\n")

print("» zadanie 3:")
print("   ", f"{majority_children[0][1]} {majority_children[0][2]} ({majority_children[1]})\n")

print("» zadanie 4:")
for parent in parent_initials:
    print("   ", parent)
print("\n")

print("» zadanie 5:")
print("   ", f"liczna kwota: {YYY}")