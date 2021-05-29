import numpy as np 

def function(x):

	r8 = 9
	l5 = 9
	paths = []
	try:
		if l5 > 7:
			x = 3/x
			r8 = r8/r8
			r8 = r8-x
			paths.append(1)
		else:
			l5 = r8-9
			paths.append(2)
		if l5 >= 0:
			x = x/3
			x = x+0
			paths.append(3)
		else:
			r8 = r8+6
			x = x-x
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))