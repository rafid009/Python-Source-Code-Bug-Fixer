import numpy as np 

def function(x):

	r6 = x
	d1 = 1
	paths = []
	try:
		if x < 5:
			r6 = 2-r6
			paths.append(1)
		else:
			r6 = r6-0
			paths.append(2)
		if r6 > 6:
			x = 1/x
			r6 = d1*7
			r6 = 2*r6
			paths.append(3)
		else:
			d1 = x*x
			r6 = r6*r6
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