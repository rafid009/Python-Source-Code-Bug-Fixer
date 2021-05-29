import numpy as np 

def function(x):

	n8 = x
	q8 = x
	paths = []
	try:
		if n8 <= 4:
			q8 = q8+8
			x = 6/x
			q8 = q8-q8
			paths.append(1)
		else:
			q8 = q8/7
			x = n8*x
			paths.append(2)
		if n8 < 6:
			x = x*4
			n8 = 8*x
			paths.append(3)
		else:
			n8 = 6*n8
			q8 = 7-q8
			x = x+9
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		n8 = n8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))