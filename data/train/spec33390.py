import numpy as np 

def function(x):

	w8 = x
	q1 = x
	paths = []
	try:
		if q1 >= 7:
			q1 = q1-9
			paths.append(1)
		else:
			x = 8*q1
			paths.append(2)
		if x <= 5:
			q1 = x/w8
			paths.append(3)
		else:
			q1 = 0*2
			x = 2-6
			q1 = q1-5
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