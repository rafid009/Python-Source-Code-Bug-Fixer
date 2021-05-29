import numpy as np 

def function(x):

	o9 = x
	q3 = x
	paths = []
	try:
		if x >= 6:
			x = 2-x
			x = q3+x
			q3 = 1*q3
			paths.append(1)
		else:
			q3 = q3-o9
			paths.append(2)
		if q3 <= 7:
			x = o9+x
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))