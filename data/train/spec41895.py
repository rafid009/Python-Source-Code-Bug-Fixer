import numpy as np 

def function(x):

	k7 = x
	k4 = x
	paths = []
	try:
		if k7 >= 8:
			k4 = k7/x
			paths.append(1)
		else:
			x = 2/k7
			k7 = x*2
			paths.append(2)
		if k7 <= 6:
			x = k4/1
			paths.append(3)
		else:
			k7 = k7*1
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