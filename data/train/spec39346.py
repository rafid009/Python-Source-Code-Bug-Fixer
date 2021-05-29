import numpy as np 

def function(x):

	f0 = 7
	l9 = 0
	paths = []
	try:
		if x >= 3:
			l9 = f0+x
			paths.append(1)
		else:
			x = f0/x
			x = 5/x
			paths.append(2)
		if f0 >= 3:
			l9 = x*x
			paths.append(3)
		else:
			l9 = f0*x
			f0 = f0*l9
			l9 = l9/x
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