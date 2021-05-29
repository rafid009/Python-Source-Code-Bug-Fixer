import numpy as np 

def function(x):

	x7 = 3
	r7 = x
	paths = []
	try:
		if x7 <= 0:
			x7 = x7*x7
			x = 9/8
			x = 1*x
			paths.append(1)
		else:
			x = x/3
			x = 0*r7
			paths.append(2)
		if x < 5:
			x7 = 0-x7
			paths.append(3)
		else:
			r7 = 0+r7
			r7 = r7/x
			x7 = r7/x7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))