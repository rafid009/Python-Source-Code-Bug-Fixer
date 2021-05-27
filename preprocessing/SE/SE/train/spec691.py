import numpy as np 

def function(x):

	q5 = x
	r0 = 9
	paths = []
	try:
		if x >= 8:
			q5 = 6-q5
			q5 = 8-3
			paths.append(1)
		else:
			x = 6*x
			r0 = 6+r0
			paths.append(2)
		if r0 < 9:
			x = 3+2
			paths.append(3)
		else:
			q5 = q5+3
			x = 6-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))