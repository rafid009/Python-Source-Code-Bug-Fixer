import numpy as np 

def function(x):

	f0 = x
	n1 = x
	x = 2
	paths = []
	try:
		if f0 <= 6:
			x = 3*x
			f0 = f0+x
			x = x-0
			paths.append(1)
		else:
			x = 6/2
			x = x+2
			n1 = x*n1
			paths.append(2)
		if x > 6:
			x = 5-1
			x = x-n1
			f0 = 9/f0
			paths.append(3)
		else:
			x = x+n1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))