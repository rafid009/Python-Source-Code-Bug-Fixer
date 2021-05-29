import numpy as np 

def function(x):

	y5 = x
	i6 = x
	paths = []
	try:
		if x > 9:
			y5 = 8-y5
			paths.append(1)
		else:
			y5 = 2*y5
			y5 = y5*y5
			x = x+4
			paths.append(2)
		if x > 1:
			i6 = i6-x
			i6 = 0/x
			x = x+2
			paths.append(3)
		else:
			x = y5*i6
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		y5 = i6**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))