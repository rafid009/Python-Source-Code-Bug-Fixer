import numpy as np 

def function(x):

	f5 = 7
	b4 = x
	paths = []
	try:
		if b4 <= 4:
			f5 = 8/7
			x = b4*9
			paths.append(1)
		else:
			x = b4*x
			b4 = b4*f5
			paths.append(2)
		if f5 >= 1:
			f5 = x-3
			x = 3*x
			paths.append(3)
		else:
			b4 = b4*2
			f5 = 9+3
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