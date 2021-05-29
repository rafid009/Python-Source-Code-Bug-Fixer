import numpy as np 

def function(x):

	q5 = x
	u0 = 3
	paths = []
	try:
		if u0 >= 9:
			u0 = x+4
			paths.append(1)
		else:
			u0 = u0-8
			q5 = 6*8
			u0 = u0+8
			paths.append(2)
		if x < 8:
			x = x/q5
			paths.append(3)
		else:
			u0 = u0*u0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))