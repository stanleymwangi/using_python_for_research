# exploring difference between shallow and deep copying
import copy

x = [38, [7]]
y = copy.copy(x)
z = copy.deepcopy(x)

# False since y is a shallow copy and references x's elements whereas z is a deep copy so has references copies of
# x's original elements
print(y is z)