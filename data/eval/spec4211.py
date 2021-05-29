import numpy as np 

def function(x):

	y6 = 8
	r8 = x
	paths = []
	try:
		if r8 <= 8:
			x = y6-x
			paths.append(1)
		else:
			x = 8-5
			r8 = 1-r8
			paths.append(2)
		if y6 > 4:
			y6 = r8+y6
			r8 = r8-0
			paths.append(3)
		else:
			r8 = r8-0
			x = y6*x
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))