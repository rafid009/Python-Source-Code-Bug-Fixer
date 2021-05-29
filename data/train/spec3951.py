import numpy as np 

def function(x):

	y2 = 0
	f1 = x
	paths = []
	try:
		if y2 < 3:
			y2 = y2-4
			x = y2*x
			f1 = 8/f1
			paths.append(1)
		else:
			x = x*x
			f1 = 0+f1
			x = x-2
			paths.append(2)
		if x > 3:
			x = x-x
			f1 = x-f1
			x = x+y2
			paths.append(3)
		else:
			f1 = 1/f1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))