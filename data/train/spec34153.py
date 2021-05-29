import numpy as np 

def function(x):

	y6 = x
	k7 = x
	paths = []
	try:
		if x > 7:
			x = 9+3
			x = 9/7
			y6 = 3/9
			paths.append(1)
		else:
			k7 = 5/k7
			k7 = k7+k7
			y6 = k7/k7
			paths.append(2)
		if k7 > 5:
			y6 = y6+y6
			x = 5+k7
			paths.append(3)
		else:
			y6 = 0*y6
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))