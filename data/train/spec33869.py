import numpy as np 

def function(x):

	n3 = 5
	y2 = x
	paths = []
	try:
		if n3 <= 1:
			x = 5-5
			y2 = 0/5
			paths.append(1)
		else:
			n3 = n3/1
			y2 = x-5
			n3 = n3/x
			paths.append(2)
		if x >= 9:
			y2 = y2-7
			paths.append(3)
		else:
			y2 = y2*y2
			x = 8-7
			y2 = y2*n3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))