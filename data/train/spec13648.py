import numpy as np 

def function(x):

	y5 = 5
	d4 = 8
	paths = []
	try:
		if d4 < 4:
			x = x+5
			paths.append(1)
		else:
			y5 = 4/8
			paths.append(2)
		if d4 <= 6:
			x = 5*9
			paths.append(3)
		else:
			y5 = x/3
			x = 5/5
			y5 = 2*y5
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