import numpy as np 

def function(x):

	r0 = 5
	w5 = 3
	paths = []
	try:
		if r0 <= 1:
			x = x+r0
			r0 = r0+8
			paths.append(1)
		else:
			r0 = 3+x
			x = x+x
			paths.append(2)
		if x > 1:
			w5 = r0*3
			x = r0/x
			paths.append(3)
		else:
			x = x*r0
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