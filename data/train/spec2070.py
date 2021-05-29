import numpy as np 

def function(x):

	r2 = 4
	l0 = x
	paths = []
	try:
		if x > 2:
			x = 7/x
			r2 = r2+l0
			paths.append(1)
		else:
			r2 = 5+l0
			l0 = x+5
			paths.append(2)
		if l0 < 2:
			r2 = 0*7
			paths.append(3)
		else:
			l0 = x/7
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		r2 = l0**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))