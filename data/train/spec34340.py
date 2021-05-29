import numpy as np 

def function(x):

	q4 = 4
	n7 = 1
	paths = []
	try:
		if n7 >= 1:
			n7 = x-n7
			x = 8+9
			paths.append(1)
		else:
			x = x+3
			n7 = q4*9
			paths.append(2)
		if q4 <= 6:
			q4 = n7+n7
			paths.append(3)
		else:
			x = n7-1
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		x = q4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))