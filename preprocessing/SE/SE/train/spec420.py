import numpy as np 

def function(x):

	l0 = x
	r8 = x
	paths = []
	try:
		if r8 < 4:
			l0 = 8*l0
			r8 = 1-r8
			paths.append(1)
		else:
			r8 = r8-l0
			l0 = 9*9
			paths.append(2)
		if l0 < 0:
			r8 = r8-4
			r8 = l0*8
			paths.append(3)
		else:
			l0 = 0-l0
			r8 = 2*r8
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))