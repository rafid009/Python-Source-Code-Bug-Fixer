import numpy as np 

def function(x):

	f0 = x
	f7 = x
	paths = []
	try:
		if x >= 6:
			f7 = 3-f7
			x = f0-5
			paths.append(1)
		else:
			x = x-6
			f7 = f0/3
			f7 = f7*7
			paths.append(2)
		if f0 > 9:
			f0 = 0*f0
			f0 = f7/2
			f0 = f0/6
			paths.append(3)
		else:
			f7 = 0+0
			x = x-1
			x = 8*x
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