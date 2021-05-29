import numpy as np 

def function(x):

	b8 = 4
	q1 = 1
	paths = []
	try:
		if q1 > 6:
			q1 = b8*q1
			b8 = b8/1
			paths.append(1)
		else:
			x = q1/x
			paths.append(2)
		if q1 > 7:
			b8 = b8/1
			q1 = 8*1
			x = x+x
			paths.append(3)
		else:
			q1 = 8+q1
			b8 = x*4
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))