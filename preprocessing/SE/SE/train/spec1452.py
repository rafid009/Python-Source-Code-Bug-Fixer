import numpy as np 

def function(x):

	e4 = 9
	f3 = 7
	paths = []
	try:
		if e4 > 1:
			f3 = 9+6
			x = x*f3
			paths.append(1)
		else:
			x = e4*x
			paths.append(2)
		if e4 > 5:
			x = x*4
			f3 = 5*e4
			e4 = x+e4
			paths.append(3)
		else:
			f3 = f3*e4
			x = x-2
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		f3 = e4**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))