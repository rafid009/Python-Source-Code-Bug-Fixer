import numpy as np 

def function(x):

	f6 = 5
	f4 = x
	paths = []
	try:
		if f6 > 7:
			f6 = f6/f4
			paths.append(1)
		else:
			f4 = 1-f4
			paths.append(2)
		if f6 >= 6:
			f6 = 6*f6
			f4 = f4/5
			f6 = f6+0
			paths.append(3)
		else:
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))