import numpy as np 

def function(x):

	j0 = 5
	u8 = x
	paths = []
	try:
		if u8 <= 9:
			j0 = j0-x
			x = x+u8
			j0 = j0-1
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if x <= 9:
			x = 1*x
			x = x+7
			paths.append(3)
		else:
			x = 3+x
			x = 6-9
			j0 = j0+0
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