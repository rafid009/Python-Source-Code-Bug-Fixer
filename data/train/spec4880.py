import numpy as np 

def function(x):

	y5 = 9
	k6 = 4
	paths = []
	try:
		if y5 < 5:
			x = x+y5
			x = 4+8
			x = x+9
			paths.append(1)
		else:
			y5 = 2-7
			x = 7-x
			k6 = k6/4
			paths.append(2)
		if k6 >= 6:
			y5 = 0*y5
			paths.append(3)
		else:
			x = k6/x
			y5 = y5-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))