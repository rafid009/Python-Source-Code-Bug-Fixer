import numpy as np 

def function(x):

	z3 = x
	o6 = x
	x = x
	paths = []
	try:
		if z3 >= 2:
			x = x*2
			paths.append(1)
		else:
			x = 8/2
			paths.append(2)
		if z3 < 8:
			x = 2-x
			x = x/3
			paths.append(3)
		else:
			x = 5/7
			o6 = z3/3
			o6 = x-o6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		z3 = o6**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))