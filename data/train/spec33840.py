import numpy as np 

def function(x):

	r0 = x
	l8 = 3
	paths = []
	try:
		if r0 > 4:
			l8 = x+5
			x = x+8
			r0 = r0+8
			paths.append(1)
		else:
			x = x+l8
			paths.append(2)
		if r0 >= 4:
			r0 = 5+r0
			r0 = r0*x
			paths.append(3)
		else:
			l8 = l8+x
			l8 = 4-l8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))