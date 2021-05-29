import numpy as np 

def function(x):

	p8 = 4
	f4 = 9
	paths = []
	try:
		if p8 < 9:
			f4 = f4-4
			f4 = f4*3
			paths.append(1)
		else:
			p8 = p8*p8
			paths.append(2)
		if x > 2:
			f4 = 9+f4
			x = x-x
			paths.append(3)
		else:
			x = 1/p8
			x = x-9
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