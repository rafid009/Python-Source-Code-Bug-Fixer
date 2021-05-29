import numpy as np 

def function(x):

	r8 = x
	a5 = 5
	paths = []
	try:
		if a5 >= 4:
			x = 5+x
			r8 = 1+x
			paths.append(1)
		else:
			r8 = r8+3
			r8 = 1-a5
			paths.append(2)
		if r8 > 6:
			x = x*x
			x = x-a5
			r8 = 2*8
			paths.append(3)
		else:
			r8 = r8-x
			a5 = 0-x
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