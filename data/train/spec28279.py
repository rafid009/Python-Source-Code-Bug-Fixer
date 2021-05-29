import numpy as np 

def function(x):

	r8 = 8
	r0 = 2
	paths = []
	try:
		if r8 < 5:
			r8 = 3+5
			r0 = r0/r0
			paths.append(1)
		else:
			x = 0-x
			paths.append(2)
		if r8 >= 7:
			r0 = r0*9
			paths.append(3)
		else:
			r0 = 0+r0
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