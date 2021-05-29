import numpy as np 

def function(x):

	q1 = 3
	b4 = 1
	paths = []
	try:
		if x >= 9:
			b4 = 7/x
			paths.append(1)
		else:
			b4 = 8+b4
			x = 0*x
			q1 = q1+x
			paths.append(2)
		if q1 >= 5:
			b4 = 9/b4
			paths.append(3)
		else:
			b4 = b4-q1
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))