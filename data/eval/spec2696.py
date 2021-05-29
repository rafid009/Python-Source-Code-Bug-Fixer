import numpy as np 

def function(x):

	x0 = x
	r2 = 7
	paths = []
	try:
		if r2 >= 7:
			x0 = 4+4
			paths.append(1)
		else:
			r2 = 2*3
			paths.append(2)
		if x >= 2:
			x0 = 5-x0
			r2 = r2*0
			paths.append(3)
		else:
			x0 = x*6
			r2 = x0*r2
			x0 = x0-0
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r2 = r2**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))