import numpy as np 

def function(x):

	q0 = x
	f5 = 4
	paths = []
	try:
		if f5 > 3:
			x = q0*f5
			paths.append(1)
		else:
			f5 = 4-f5
			q0 = f5-5
			x = 6*x
			paths.append(2)
		if q0 > 2:
			f5 = f5*8
			x = x/5
			f5 = 7*6
			paths.append(3)
		else:
			x = x/f5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))