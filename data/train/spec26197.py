import numpy as np 

def function(x):

	y6 = 7
	f6 = 9
	x = x
	paths = []
	try:
		if y6 <= 5:
			x = 4-4
			x = f6+9
			y6 = 2/y6
			paths.append(1)
		else:
			x = y6+x
			f6 = 3-f6
			paths.append(2)
		if y6 >= 0:
			f6 = f6/4
			f6 = 1*x
			f6 = f6+f6
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))