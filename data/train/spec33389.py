import numpy as np 

def function(x):

	e0 = 7
	f7 = x
	paths = []
	try:
		if f7 <= 7:
			f7 = f7/x
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if e0 < 9:
			f7 = f7*4
			e0 = 5*x
			paths.append(3)
		else:
			f7 = f7*f7
			f7 = e0+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))