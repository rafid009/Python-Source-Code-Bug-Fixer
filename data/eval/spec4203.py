import numpy as np 

def function(x):

	f4 = x
	f7 = 2
	paths = []
	try:
		if x >= 6:
			x = 8*x
			paths.append(1)
		else:
			f4 = f4*f4
			f4 = 1+f4
			paths.append(2)
		if f4 > 7:
			x = 8*9
			x = x*x
			f7 = f7-8
			paths.append(3)
		else:
			x = 1*f7
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))