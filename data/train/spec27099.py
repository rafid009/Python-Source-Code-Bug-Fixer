import numpy as np 

def function(x):

	k6 = 1
	y7 = x
	paths = []
	try:
		if x >= 8:
			y7 = x/y7
			x = x-5
			paths.append(1)
		else:
			k6 = 5-k6
			paths.append(2)
		if x <= 9:
			y7 = y7-x
			x = 9+x
			k6 = k6-6
			paths.append(3)
		else:
			y7 = y7*9
			k6 = x*8
			y7 = 2/y7
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