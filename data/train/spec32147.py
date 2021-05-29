import numpy as np 

def function(x):

	i6 = 4
	y5 = x
	paths = []
	try:
		if y5 > 6:
			i6 = i6*9
			y5 = x-8
			paths.append(1)
		else:
			x = 2-x
			x = x*y5
			x = y5-7
			paths.append(2)
		if x < 7:
			y5 = 7-y5
			x = 0*y5
			paths.append(3)
		else:
			y5 = 4/y5
			x = x/1
			i6 = 1-i6
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