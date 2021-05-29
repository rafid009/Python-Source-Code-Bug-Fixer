import numpy as np 

def function(x):

	y6 = x
	k5 = 4
	paths = []
	try:
		if y6 > 2:
			y6 = y6+x
			x = x-6
			y6 = y6/6
			paths.append(1)
		else:
			x = x/k5
			x = x/y6
			paths.append(2)
		if k5 > 4:
			x = k5/4
			k5 = k5-0
			k5 = 0+k5
			paths.append(3)
		else:
			k5 = 8+2
			y6 = y6+y6
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