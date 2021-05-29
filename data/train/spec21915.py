import numpy as np 

def function(x):

	b7 = x
	r1 = x
	paths = []
	try:
		if x > 6:
			x = 6-x
			paths.append(1)
		else:
			r1 = r1/8
			paths.append(2)
		if r1 > 9:
			r1 = 2*r1
			b7 = b7+b7
			paths.append(3)
		else:
			x = b7/6
			x = x+8
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