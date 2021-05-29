import numpy as np 

def function(x):

	n8 = 1
	q4 = 5
	paths = []
	try:
		if x > 6:
			n8 = n8+5
			n8 = n8/n8
			n8 = 5-n8
			paths.append(1)
		else:
			n8 = n8/7
			paths.append(2)
		if x <= 2:
			q4 = q4*6
			paths.append(3)
		else:
			q4 = x/3
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