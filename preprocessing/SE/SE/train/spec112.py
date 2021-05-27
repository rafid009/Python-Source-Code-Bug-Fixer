import numpy as np 

def function(x):

	a4 = 1
	y6 = 6
	paths = []
	try:
		if x <= 0:
			x = x+x
			y6 = 1+y6
			x = a4-y6
			paths.append(1)
		else:
			x = a4/1
			paths.append(2)
		if a4 >= 7:
			x = x*1
			y6 = x+a4
			a4 = a4+a4
			paths.append(3)
		else:
			x = x-7
			a4 = a4+7
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