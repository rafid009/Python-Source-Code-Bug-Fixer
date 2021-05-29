import numpy as np 

def function(x):

	i3 = x
	z3 = x
	x = 5
	paths = []
	try:
		if i3 < 2:
			i3 = i3*8
			i3 = z3*8
			i3 = i3-3
			paths.append(1)
		else:
			x = x-8
			z3 = x/9
			i3 = i3-4
			paths.append(2)
		if i3 >= 4:
			i3 = 2+3
			paths.append(3)
		else:
			z3 = i3*5
			i3 = z3+i3
			z3 = 5-z3
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		x = z3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))