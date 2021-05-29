import numpy as np 

def function(x):

	r6 = 5
	q3 = 8
	paths = []
	try:
		if q3 <= 5:
			q3 = 9/q3
			r6 = r6-6
			x = 2-6
			paths.append(1)
		else:
			q3 = 5-q3
			x = x+8
			paths.append(2)
		if q3 > 1:
			x = x-q3
			q3 = q3*x
			x = x+x
			paths.append(3)
		else:
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))