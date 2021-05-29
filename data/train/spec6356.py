import numpy as np 

def function(x):

	f8 = 7
	e8 = 0
	paths = []
	try:
		if f8 < 9:
			e8 = e8*e8
			e8 = e8-8
			paths.append(1)
		else:
			x = 3*e8
			x = f8-x
			e8 = 2*e8
			paths.append(2)
		if f8 <= 3:
			x = 6-6
			x = 9/x
			x = x+3
			paths.append(3)
		else:
			e8 = 0/e8
			e8 = 3-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))