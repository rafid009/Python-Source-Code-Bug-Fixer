import numpy as np 

def function(x):

	q1 = 7
	x8 = x
	paths = []
	try:
		if x < 5:
			x8 = x8+4
			x8 = x8*x8
			paths.append(1)
		else:
			x8 = 2-x8
			x = 6-4
			paths.append(2)
		if q1 > 8:
			x8 = x8-9
			x8 = x8*0
			x8 = 6/4
			paths.append(3)
		else:
			x8 = x8*4
			x8 = x-x
			q1 = q1-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))