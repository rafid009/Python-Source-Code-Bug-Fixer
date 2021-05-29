import numpy as np 

def function(x):

	a9 = x
	f6 = 5
	paths = []
	try:
		if x >= 8:
			f6 = f6/3
			a9 = 8+7
			paths.append(1)
		else:
			a9 = 0-a9
			paths.append(2)
		if a9 < 7:
			x = 4*x
			paths.append(3)
		else:
			a9 = a9/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))