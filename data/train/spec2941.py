import numpy as np 

def function(x):

	x2 = x
	f8 = x
	paths = []
	try:
		if x >= 5:
			x = x-x2
			f8 = x/f8
			f8 = f8-8
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if f8 > 0:
			f8 = 2+6
			x2 = 6+1
			x = 8/x
			paths.append(3)
		else:
			x2 = x2/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))