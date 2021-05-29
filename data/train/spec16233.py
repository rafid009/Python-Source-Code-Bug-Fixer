import numpy as np 

def function(x):

	r3 = x
	y5 = 8
	paths = []
	try:
		if r3 >= 6:
			y5 = y5*y5
			r3 = r3/2
			paths.append(1)
		else:
			r3 = r3/y5
			paths.append(2)
		if x > 3:
			y5 = 8-y5
			y5 = 4+y5
			paths.append(3)
		else:
			r3 = r3+7
			x = 4+2
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))