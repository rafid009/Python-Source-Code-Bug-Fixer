import numpy as np 

def function(x):

	f3 = x
	y1 = x
	paths = []
	try:
		if f3 >= 2:
			x = x-y1
			paths.append(1)
		else:
			f3 = f3+3
			x = y1+x
			paths.append(2)
		if x >= 8:
			y1 = x-0
			y1 = y1*y1
			f3 = f3/7
			paths.append(3)
		else:
			x = y1/7
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		y1 = f3**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))