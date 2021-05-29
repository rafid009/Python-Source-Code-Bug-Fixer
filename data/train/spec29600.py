import numpy as np 

def function(x):

	o4 = x
	r1 = 2
	paths = []
	try:
		if x > 7:
			x = o4+x
			x = 0-r1
			paths.append(1)
		else:
			r1 = 5*r1
			r1 = r1+0
			r1 = r1-7
			paths.append(2)
		if r1 > 7:
			x = r1/x
			x = o4/x
			o4 = 3/o4
			paths.append(3)
		else:
			x = 9+x
			r1 = x+r1
			x = 6/o4
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