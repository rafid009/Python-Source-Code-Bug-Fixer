import numpy as np 

def function(x):

	f9 = x
	y1 = 6
	paths = []
	try:
		if y1 > 6:
			x = 5+y1
			paths.append(1)
		else:
			y1 = x*1
			x = 1/y1
			paths.append(2)
		if x <= 8:
			y1 = f9-y1
			f9 = f9-9
			y1 = 0-x
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		y1 = f9**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))