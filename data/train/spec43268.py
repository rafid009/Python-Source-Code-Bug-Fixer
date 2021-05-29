import numpy as np 

def function(x):

	o4 = x
	n6 = x
	paths = []
	try:
		if n6 >= 0:
			x = n6+x
			x = x*9
			paths.append(1)
		else:
			n6 = o4*0
			n6 = 7*o4
			paths.append(2)
		if n6 >= 0:
			n6 = 5*n6
			paths.append(3)
		else:
			o4 = 9+o4
			o4 = 4/o4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))