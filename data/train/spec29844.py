import numpy as np 

def function(x):

	f4 = 2
	y1 = x
	paths = []
	try:
		if f4 > 6:
			f4 = f4/9
			y1 = y1+y1
			y1 = y1/6
			paths.append(1)
		else:
			y1 = y1+1
			paths.append(2)
		if f4 > 9:
			y1 = 8*y1
			paths.append(3)
		else:
			f4 = f4/x
			y1 = y1*2
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))