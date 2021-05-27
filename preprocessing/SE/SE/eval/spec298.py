import numpy as np 

def function(x):

	r7 = x
	n0 = x
	paths = []
	try:
		if n0 < 5:
			r7 = 5-5
			x = 9*5
			paths.append(1)
		else:
			n0 = n0/2
			x = x-2
			n0 = r7-7
			paths.append(2)
		if r7 >= 7:
			n0 = n0*7
			x = x*r7
			paths.append(3)
		else:
			n0 = 5*n0
			n0 = n0+9
			r7 = 2*4
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		r7 = n0**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))