import numpy as np 

def function(x):

	n2 = x
	a7 = 4
	paths = []
	try:
		if x <= 1:
			x = 8+9
			a7 = 9+n2
			paths.append(1)
		else:
			a7 = x/a7
			a7 = 3*6
			paths.append(2)
		if x < 7:
			x = 1+2
			n2 = 8/2
			a7 = a7-0
			paths.append(3)
		else:
			x = x/a7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))