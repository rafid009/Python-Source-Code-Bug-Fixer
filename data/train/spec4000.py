import numpy as np 

def function(x):

	k1 = 7
	q4 = 7
	paths = []
	try:
		if k1 > 2:
			q4 = q4*9
			x = x+q4
			q4 = q4/2
			paths.append(1)
		else:
			q4 = 7/8
			paths.append(2)
		if q4 < 2:
			q4 = 9/2
			k1 = k1+x
			x = 9-2
			paths.append(3)
		else:
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))