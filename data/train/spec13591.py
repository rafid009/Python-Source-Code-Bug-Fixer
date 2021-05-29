import numpy as np 

def function(x):

	f6 = x
	l7 = 8
	paths = []
	try:
		if x > 9:
			x = x*9
			x = x+f6
			x = 2-x
			paths.append(1)
		else:
			f6 = f6*8
			f6 = f6-4
			paths.append(2)
		if x < 8:
			x = 5+x
			paths.append(3)
		else:
			x = 9-x
			f6 = f6-4
			x = x+5
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