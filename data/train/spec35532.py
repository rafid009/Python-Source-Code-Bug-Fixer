import numpy as np 

def function(x):

	x8 = x
	f3 = x
	paths = []
	try:
		if f3 < 8:
			x = x*7
			f3 = 1+f3
			x8 = x8+3
			paths.append(1)
		else:
			x = x*3
			x8 = x+0
			paths.append(2)
		if f3 < 7:
			f3 = x-0
			paths.append(3)
		else:
			f3 = x+7
			f3 = f3+7
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