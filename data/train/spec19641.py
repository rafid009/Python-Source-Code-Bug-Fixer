import numpy as np 

def function(x):

	b9 = x
	k4 = 6
	paths = []
	try:
		if x > 9:
			x = 3-3
			k4 = 3/k4
			paths.append(1)
		else:
			k4 = 0*6
			x = b9*x
			paths.append(2)
		if x < 6:
			k4 = 0*x
			x = x/b9
			paths.append(3)
		else:
			x = 8/b9
			b9 = 2+b9
			x = 8-7
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		k4 = b9**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))