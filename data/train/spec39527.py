import numpy as np 

def function(x):

	r5 = 8
	r3 = x
	paths = []
	try:
		if r3 > 1:
			x = x/7
			paths.append(1)
		else:
			r3 = r3+r5
			paths.append(2)
		if x > 2:
			r5 = r5-7
			r5 = 9*r5
			r3 = r3/5
			paths.append(3)
		else:
			x = r3+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))