import numpy as np 

def function(x):

	f6 = x
	t8 = 5
	paths = []
	try:
		if x <= 2:
			f6 = t8/t8
			paths.append(1)
		else:
			f6 = 9+t8
			t8 = t8-f6
			x = x+7
			paths.append(2)
		if x < 9:
			x = x-2
			f6 = 1-f6
			f6 = 4*x
			paths.append(3)
		else:
			t8 = 0+f6
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