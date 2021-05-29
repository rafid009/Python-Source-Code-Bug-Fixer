import numpy as np 

def function(x):

	f4 = 8
	y5 = x
	paths = []
	try:
		if f4 < 7:
			x = 3*x
			paths.append(1)
		else:
			x = 4/x
			x = 4+x
			paths.append(2)
		if x >= 5:
			y5 = 9+5
			x = f4/x
			paths.append(3)
		else:
			y5 = y5/6
			f4 = f4-4
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))