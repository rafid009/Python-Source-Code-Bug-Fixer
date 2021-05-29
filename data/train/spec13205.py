import numpy as np 

def function(x):

	r9 = 1
	v8 = x
	paths = []
	try:
		if x >= 3:
			r9 = 5+8
			r9 = r9*8
			v8 = 1*v8
			paths.append(1)
		else:
			r9 = 9/r9
			r9 = 8+r9
			v8 = v8+7
			paths.append(2)
		if x >= 1:
			r9 = 0*r9
			v8 = v8*r9
			v8 = v8+x
			paths.append(3)
		else:
			v8 = v8*r9
			x = 7*x
			v8 = r9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))