import numpy as np 

def function(x):

	r1 = 2
	q2 = x
	paths = []
	try:
		if x <= 2:
			q2 = q2/1
			paths.append(1)
		else:
			r1 = 4*r1
			paths.append(2)
		if r1 >= 7:
			x = x-3
			r1 = x*r1
			x = x-2
			paths.append(3)
		else:
			r1 = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))