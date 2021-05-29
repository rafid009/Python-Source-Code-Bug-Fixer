import numpy as np 

def function(x):

	y6 = 8
	f2 = x
	paths = []
	try:
		if y6 <= 0:
			y6 = 2-y6
			x = 6/2
			paths.append(1)
		else:
			y6 = 5+0
			paths.append(2)
		if x >= 4:
			f2 = f2*3
			x = 5-8
			f2 = f2-f2
			paths.append(3)
		else:
			f2 = f2*0
			x = 1-x
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