import numpy as np 

def function(x):

	k5 = 1
	x6 = x
	paths = []
	try:
		if k5 <= 6:
			x = x+2
			x = x*4
			k5 = 3+k5
			paths.append(1)
		else:
			x6 = k5-x6
			paths.append(2)
		if x < 8:
			x6 = k5/x6
			paths.append(3)
		else:
			k5 = x6-k5
			x = x6-x
			x6 = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))