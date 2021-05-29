import numpy as np 

def function(x):

	v0 = 2
	r0 = x
	paths = []
	try:
		if v0 >= 1:
			x = x+x
			r0 = r0-v0
			x = 8*x
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if r0 >= 7:
			r0 = 3-r0
			v0 = 3-r0
			paths.append(3)
		else:
			x = v0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))