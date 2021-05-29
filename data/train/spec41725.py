import numpy as np 

def function(x):

	u0 = x
	f5 = x
	paths = []
	try:
		if u0 <= 8:
			x = x/9
			f5 = f5/9
			x = x/2
			paths.append(1)
		else:
			u0 = f5-6
			f5 = f5*x
			paths.append(2)
		if x <= 4:
			u0 = 3*3
			f5 = 8/f5
			x = 1/x
			paths.append(3)
		else:
			f5 = u0*5
			u0 = 7*u0
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