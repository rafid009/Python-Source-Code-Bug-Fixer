import numpy as np 

def function(x):

	z3 = x
	w3 = 4
	x = 1
	paths = []
	try:
		if z3 < 9:
			w3 = w3*2
			x = 1+x
			paths.append(1)
		else:
			x = 6/1
			paths.append(2)
		if z3 >= 7:
			z3 = x+8
			x = x-x
			w3 = 1-0
			paths.append(3)
		else:
			w3 = w3+4
			x = 4+z3
			x = x+1
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		w3 = z3**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))