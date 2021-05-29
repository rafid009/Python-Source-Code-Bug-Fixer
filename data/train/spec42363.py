import numpy as np 

def function(x):

	r0 = 5
	y6 = x
	paths = []
	try:
		if x >= 4:
			x = r0/7
			y6 = y6*x
			x = 9*9
			paths.append(1)
		else:
			r0 = r0+6
			x = 2/y6
			paths.append(2)
		if x >= 7:
			y6 = 4+1
			paths.append(3)
		else:
			x = x+4
			r0 = x-r0
			r0 = r0+5
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		r0 = y6**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))