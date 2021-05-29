import numpy as np 

def function(x):

	n4 = x
	f9 = x
	paths = []
	try:
		if f9 < 5:
			n4 = 8*1
			paths.append(1)
		else:
			f9 = f9*7
			paths.append(2)
		if f9 <= 2:
			n4 = n4*f9
			paths.append(3)
		else:
			x = 3-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))