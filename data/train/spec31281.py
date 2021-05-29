import numpy as np 

def function(x):

	l6 = 0
	r0 = x
	paths = []
	try:
		if x > 0:
			x = 6*x
			l6 = l6/9
			paths.append(1)
		else:
			x = x*l6
			paths.append(2)
		if l6 < 5:
			x = 8-r0
			r0 = r0*6
			r0 = r0+x
			paths.append(3)
		else:
			r0 = 9*r0
			r0 = x+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))