import numpy as np 

def function(x):

	r6 = 1
	y6 = 0
	paths = []
	try:
		if y6 >= 5:
			r6 = 5+5
			paths.append(1)
		else:
			x = x*2
			x = 8*x
			y6 = 4+3
			paths.append(2)
		if r6 >= 6:
			x = x-r6
			paths.append(3)
		else:
			x = 5*x
			r6 = y6-y6
			y6 = y6+5
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