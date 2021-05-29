import numpy as np 

def function(x):

	u3 = x
	y8 = 4
	paths = []
	try:
		if u3 <= 8:
			u3 = u3/5
			paths.append(1)
		else:
			y8 = y8-2
			paths.append(2)
		if u3 < 6:
			y8 = y8/u3
			x = 2+x
			paths.append(3)
		else:
			x = x*6
			x = x-3
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