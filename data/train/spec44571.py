import numpy as np 

def function(x):

	r5 = 4
	v7 = 6
	paths = []
	try:
		if x > 3:
			r5 = r5-2
			x = r5/x
			paths.append(1)
		else:
			v7 = v7/v7
			paths.append(2)
		if r5 < 0:
			v7 = 9+v7
			r5 = 2*r5
			r5 = 3/r5
			paths.append(3)
		else:
			r5 = 5*0
			r5 = r5/6
			r5 = r5/x
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