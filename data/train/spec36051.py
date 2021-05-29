import numpy as np 

def function(x):

	f3 = 3
	f8 = 2
	paths = []
	try:
		if f8 >= 4:
			x = f8+f8
			f3 = 1*f8
			paths.append(1)
		else:
			f3 = 7-6
			f3 = f3-2
			f8 = 7/7
			paths.append(2)
		if f8 < 9:
			f3 = 3*f3
			f8 = 3*f3
			f3 = f3/3
			paths.append(3)
		else:
			f3 = 3-f3
			f8 = f8*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f3 = x**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))