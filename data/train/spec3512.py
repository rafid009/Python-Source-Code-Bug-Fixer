import numpy as np 

def function(x):

	l0 = x
	a8 = x
	paths = []
	try:
		if a8 >= 7:
			a8 = x+x
			l0 = l0*x
			x = 4*a8
			paths.append(1)
		else:
			x = x-0
			paths.append(2)
		if a8 >= 1:
			x = a8*x
			paths.append(3)
		else:
			x = x-a8
			a8 = a8*0
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))