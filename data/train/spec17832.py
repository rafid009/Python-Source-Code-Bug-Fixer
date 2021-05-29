import numpy as np 

def function(x):

	x9 = x
	k5 = 3
	paths = []
	try:
		if x <= 2:
			x9 = x9/1
			paths.append(1)
		else:
			k5 = 5+k5
			k5 = k5/9
			paths.append(2)
		if x9 >= 8:
			x = x-x
			x9 = x*x9
			paths.append(3)
		else:
			k5 = k5*9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))