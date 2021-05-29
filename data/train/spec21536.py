import numpy as np 

def function(x):

	k7 = 5
	j5 = 3
	paths = []
	try:
		if x < 5:
			x = 2-x
			paths.append(1)
		else:
			x = x-5
			k7 = k7-x
			j5 = x+k7
			paths.append(2)
		if k7 < 5:
			k7 = 0+9
			k7 = k7-3
			k7 = k7+1
			paths.append(3)
		else:
			j5 = 7-j5
			k7 = k7/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))