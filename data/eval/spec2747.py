import numpy as np 

def function(x):

	r5 = x
	x8 = x
	paths = []
	try:
		if r5 < 5:
			x = 8-6
			x = 9*x
			x = x8+x
			paths.append(1)
		else:
			x8 = 5-x
			x8 = x8-2
			x = 2/6
			paths.append(2)
		if x <= 5:
			x8 = x8*x
			x8 = 6+1
			paths.append(3)
		else:
			x8 = x8-9
			x8 = 1/7
			x = r5/x
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