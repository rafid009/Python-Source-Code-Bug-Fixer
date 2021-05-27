import numpy as np 

def function(x):

	e7 = x
	k5 = 7
	paths = []
	try:
		if e7 < 2:
			x = 4+x
			k5 = 7*k5
			paths.append(1)
		else:
			k5 = 0-2
			paths.append(2)
		if x <= 3:
			e7 = e7*8
			k5 = 8*6
			x = k5*k5
			paths.append(3)
		else:
			e7 = 4-e7
			e7 = k5+7
			k5 = k5/4
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		x = k5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))