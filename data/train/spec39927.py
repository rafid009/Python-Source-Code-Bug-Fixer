import numpy as np 

def function(x):

	n3 = 1
	r5 = 7
	paths = []
	try:
		if r5 <= 7:
			r5 = r5*2
			r5 = 3*r5
			paths.append(1)
		else:
			r5 = 6-5
			n3 = n3-9
			n3 = n3-5
			paths.append(2)
		if n3 <= 0:
			x = 6*x
			paths.append(3)
		else:
			n3 = 3*5
			n3 = n3*7
			r5 = 4/r5
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