import numpy as np 

def function(x):

	n3 = x
	q7 = x
	paths = []
	try:
		if q7 <= 5:
			n3 = x/1
			x = x+8
			paths.append(1)
		else:
			q7 = n3*q7
			x = 9-x
			paths.append(2)
		if q7 < 2:
			n3 = 0-7
			n3 = n3-4
			n3 = n3-3
			paths.append(3)
		else:
			x = x*q7
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))