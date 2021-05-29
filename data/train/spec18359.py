import numpy as np 

def function(x):

	n0 = x
	g3 = x
	paths = []
	try:
		if n0 >= 9:
			x = x-0
			x = x-9
			n0 = x*n0
			paths.append(1)
		else:
			n0 = x*n0
			paths.append(2)
		if n0 <= 7:
			n0 = 9/5
			paths.append(3)
		else:
			x = x-1
			x = 2*2
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		n0 = g3**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))