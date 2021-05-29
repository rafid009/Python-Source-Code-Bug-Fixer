import numpy as np 

def function(x):

	n5 = 9
	q1 = x
	paths = []
	try:
		if x <= 2:
			x = x-6
			n5 = 4*n5
			paths.append(1)
		else:
			n5 = 8/n5
			x = q1+1
			q1 = q1*1
			paths.append(2)
		if q1 > 3:
			n5 = 3-n5
			q1 = 8-1
			n5 = 0-n5
			paths.append(3)
		else:
			x = x*9
			x = x/3
			q1 = x*4
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