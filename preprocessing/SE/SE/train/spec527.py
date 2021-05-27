import numpy as np 

def function(x):

	f9 = 7
	l0 = x
	paths = []
	try:
		if f9 < 8:
			x = x/7
			x = x-8
			paths.append(1)
		else:
			f9 = f9-5
			l0 = l0*l0
			paths.append(2)
		if f9 >= 0:
			f9 = x-f9
			f9 = 5*l0
			f9 = 0*4
			paths.append(3)
		else:
			f9 = 7/2
			f9 = l0+l0
			x = 3+x
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