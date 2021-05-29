import numpy as np 

def function(x):

	o9 = 3
	x8 = x
	paths = []
	try:
		if x <= 7:
			x8 = x8*x
			paths.append(1)
		else:
			x8 = x8*x8
			x8 = x8/o9
			paths.append(2)
		if x > 4:
			x8 = 1*2
			paths.append(3)
		else:
			o9 = x-3
			x8 = 5+x8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))