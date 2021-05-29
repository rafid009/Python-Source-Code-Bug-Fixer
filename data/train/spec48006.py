import numpy as np 

def function(x):

	f1 = x
	y0 = x
	paths = []
	try:
		if f1 >= 8:
			x = 2+7
			y0 = 1*y0
			f1 = f1/4
			paths.append(1)
		else:
			f1 = f1*9
			paths.append(2)
		if x > 8:
			y0 = 4/y0
			f1 = f1+3
			y0 = 7-y0
			paths.append(3)
		else:
			x = x*5
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x = f1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))