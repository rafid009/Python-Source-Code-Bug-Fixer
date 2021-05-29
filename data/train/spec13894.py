import numpy as np 

def function(x):

	k5 = 9
	y4 = 5
	paths = []
	try:
		if k5 >= 2:
			y4 = 1*y4
			x = x/9
			paths.append(1)
		else:
			k5 = 6/4
			paths.append(2)
		if k5 <= 1:
			k5 = 0-6
			k5 = y4+k5
			k5 = k5-9
			paths.append(3)
		else:
			x = 1+x
			k5 = 5/3
			k5 = k5*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))