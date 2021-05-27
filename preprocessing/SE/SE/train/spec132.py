import numpy as np 

def function(x):

	q4 = 5
	r1 = 2
	paths = []
	try:
		if q4 < 7:
			r1 = r1-5
			x = 4+2
			paths.append(1)
		else:
			r1 = r1+q4
			paths.append(2)
		if x < 4:
			q4 = x*q4
			paths.append(3)
		else:
			x = r1*x
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