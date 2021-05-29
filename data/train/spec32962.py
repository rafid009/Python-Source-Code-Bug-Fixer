import numpy as np 

def function(x):

	r2 = 2
	v4 = x
	paths = []
	try:
		if v4 <= 0:
			r2 = r2+r2
			paths.append(1)
		else:
			x = 2-x
			v4 = 9*x
			v4 = 6*v4
			paths.append(2)
		if r2 >= 0:
			v4 = v4-v4
			r2 = x-3
			v4 = v4*5
			paths.append(3)
		else:
			r2 = r2*3
			v4 = 6/6
			x = x+3
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