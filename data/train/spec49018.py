import numpy as np 

def function(x):

	r7 = x
	v0 = 1
	paths = []
	try:
		if x >= 6:
			x = 8+r7
			x = x*7
			r7 = 2+r7
			paths.append(1)
		else:
			v0 = 1+v0
			r7 = r7/x
			v0 = 5-v0
			paths.append(2)
		if r7 <= 0:
			r7 = 8/r7
			paths.append(3)
		else:
			r7 = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))