import numpy as np 

def function(x):

	f5 = 6
	n1 = 1
	paths = []
	try:
		if n1 > 7:
			n1 = 8*n1
			f5 = f5-6
			paths.append(1)
		else:
			f5 = f5+3
			paths.append(2)
		if n1 < 8:
			x = x*2
			x = 3-x
			n1 = 9-f5
			paths.append(3)
		else:
			x = x-f5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))