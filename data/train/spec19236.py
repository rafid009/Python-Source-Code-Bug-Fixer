import numpy as np 

def function(x):

	q3 = 0
	k2 = x
	paths = []
	try:
		if k2 >= 1:
			k2 = k2-x
			x = x+4
			x = x+8
			paths.append(1)
		else:
			k2 = q3+k2
			paths.append(2)
		if x <= 3:
			k2 = k2-1
			paths.append(3)
		else:
			q3 = x-4
			x = 2*x
			q3 = x-q3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))