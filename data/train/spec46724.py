import numpy as np 

def function(x):

	e9 = x
	n2 = 1
	x = x
	paths = []
	try:
		if x > 2:
			n2 = 5*8
			n2 = n2/3
			n2 = n2-9
			paths.append(1)
		else:
			n2 = x-e9
			paths.append(2)
		if n2 >= 0:
			x = x+e9
			n2 = n2-3
			paths.append(3)
		else:
			e9 = e9-e9
			n2 = n2-4
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))