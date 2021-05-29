import numpy as np 

def function(x):

	l7 = x
	r2 = 4
	paths = []
	try:
		if x <= 2:
			x = 4+x
			r2 = r2+r2
			paths.append(1)
		else:
			r2 = r2*l7
			paths.append(2)
		if l7 > 2:
			l7 = l7-2
			r2 = 6-r2
			l7 = x/x
			paths.append(3)
		else:
			r2 = 9*r2
			l7 = l7+8
			x = x*9
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