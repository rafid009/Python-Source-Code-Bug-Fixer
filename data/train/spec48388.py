import numpy as np 

def function(x):

	y5 = 0
	f7 = 1
	paths = []
	try:
		if x <= 3:
			f7 = 1+x
			paths.append(1)
		else:
			x = 3+x
			x = x*x
			paths.append(2)
		if x <= 1:
			y5 = y5+y5
			f7 = 4*x
			x = x-f7
			paths.append(3)
		else:
			y5 = y5-2
			f7 = f7+f7
			y5 = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))