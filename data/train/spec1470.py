import numpy as np 

def function(x):

	q7 = x
	r2 = x
	paths = []
	try:
		if q7 <= 2:
			r2 = 2*0
			r2 = r2+8
			paths.append(1)
		else:
			x = x+8
			r2 = r2*x
			paths.append(2)
		if r2 > 1:
			q7 = q7-6
			r2 = r2-q7
			x = x-5
			paths.append(3)
		else:
			q7 = q7/2
			x = q7+4
			q7 = q7/x
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