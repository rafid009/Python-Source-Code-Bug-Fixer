import numpy as np 

def function(x):

	q7 = 3
	r9 = 0
	paths = []
	try:
		if r9 > 0:
			x = q7+x
			r9 = 1*r9
			paths.append(1)
		else:
			r9 = 3+7
			r9 = q7+r9
			paths.append(2)
		if r9 > 9:
			r9 = x-x
			paths.append(3)
		else:
			r9 = r9*2
			r9 = r9*3
			q7 = q7+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))