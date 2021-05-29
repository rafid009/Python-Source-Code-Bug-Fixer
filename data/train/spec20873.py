import numpy as np 

def function(x):

	z7 = 5
	x8 = x
	paths = []
	try:
		if z7 >= 9:
			x = 1+x
			x = 3*x
			x = z7*3
			paths.append(1)
		else:
			x8 = 5*x8
			paths.append(2)
		if x8 < 9:
			x = x+8
			x8 = x8+z7
			paths.append(3)
		else:
			x8 = 7+9
			x8 = x8/x
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))