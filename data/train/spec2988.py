import numpy as np 

def function(x):

	n8 = 0
	q3 = 1
	paths = []
	try:
		if q3 <= 1:
			q3 = 1*5
			q3 = 8+6
			paths.append(1)
		else:
			q3 = q3/9
			x = 1-0
			paths.append(2)
		if x < 3:
			x = x-9
			paths.append(3)
		else:
			n8 = n8-n8
			n8 = 5/5
			q3 = 9/q3
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