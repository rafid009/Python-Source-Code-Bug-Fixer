import numpy as np 

def function(x):

	l0 = 8
	u0 = x
	paths = []
	try:
		if l0 >= 1:
			x = x-8
			paths.append(1)
		else:
			l0 = 7+2
			u0 = u0-7
			x = x+5
			paths.append(2)
		if u0 >= 8:
			x = 3*x
			u0 = l0*u0
			paths.append(3)
		else:
			x = 0/l0
			x = x*0
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		x = u0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))