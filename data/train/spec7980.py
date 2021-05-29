import numpy as np 

def function(x):

	f9 = 6
	f4 = 6
	paths = []
	try:
		if x < 3:
			f4 = f4/9
			f9 = f4+f9
			f4 = 9*f4
			paths.append(1)
		else:
			f4 = f4+7
			f9 = f9-f9
			f4 = 9*f4
			paths.append(2)
		if x < 8:
			x = 7*x
			paths.append(3)
		else:
			f9 = x-2
			f4 = x*8
			x = x-0
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