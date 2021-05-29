import numpy as np 

def function(x):

	n7 = 2
	f7 = 4
	paths = []
	try:
		if x <= 2:
			x = 8/x
			paths.append(1)
		else:
			f7 = 1+f7
			paths.append(2)
		if n7 <= 8:
			f7 = f7-0
			x = 2-8
			paths.append(3)
		else:
			f7 = 7+f7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))