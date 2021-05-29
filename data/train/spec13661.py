import numpy as np 

def function(x):

	t2 = 9
	x8 = x
	paths = []
	try:
		if x >= 6:
			x = 6-x
			x = 8+x
			paths.append(1)
		else:
			t2 = t2-8
			paths.append(2)
		if x8 >= 3:
			x8 = x8-8
			t2 = 6/7
			x8 = x8*7
			paths.append(3)
		else:
			x8 = 1+x8
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