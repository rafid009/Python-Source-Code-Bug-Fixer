import numpy as np 

def function(x):

	f8 = 5
	x9 = 4
	paths = []
	try:
		if f8 > 4:
			f8 = 6-7
			f8 = f8*f8
			x9 = x9-x9
			paths.append(1)
		else:
			x9 = x9/7
			x = 6+1
			paths.append(2)
		if x >= 2:
			f8 = 6-f8
			x = x/9
			paths.append(3)
		else:
			x = x/f8
			x = x+2
			x9 = 9-9
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