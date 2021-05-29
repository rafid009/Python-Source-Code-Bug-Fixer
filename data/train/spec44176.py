import numpy as np 

def function(x):

	k4 = 8
	b6 = x
	paths = []
	try:
		if x <= 1:
			x = x+x
			x = x-x
			k4 = k4*k4
			paths.append(1)
		else:
			x = b6-8
			paths.append(2)
		if k4 < 7:
			b6 = k4+b6
			paths.append(3)
		else:
			k4 = k4*b6
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))