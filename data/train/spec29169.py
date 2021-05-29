import numpy as np 

def function(x):

	q4 = 1
	n5 = 3
	paths = []
	try:
		if x <= 6:
			n5 = n5/n5
			q4 = n5-n5
			q4 = q4/6
			paths.append(1)
		else:
			x = x/4
			x = x/7
			paths.append(2)
		if n5 < 8:
			n5 = 4-n5
			paths.append(3)
		else:
			q4 = q4*8
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