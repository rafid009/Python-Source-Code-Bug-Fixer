import numpy as np 

def function(x):

	r6 = x
	q3 = 0
	paths = []
	try:
		if x >= 5:
			x = r6*8
			paths.append(1)
		else:
			q3 = 4-q3
			paths.append(2)
		if q3 > 4:
			r6 = 7+3
			paths.append(3)
		else:
			q3 = q3+x
			r6 = 0-r6
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