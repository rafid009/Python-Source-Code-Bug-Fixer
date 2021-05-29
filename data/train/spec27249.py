import numpy as np 

def function(x):

	f4 = 5
	y5 = x
	paths = []
	try:
		if x < 0:
			x = x/7
			y5 = 5*3
			f4 = y5-3
			paths.append(1)
		else:
			f4 = y5*f4
			y5 = 4/y5
			paths.append(2)
		if f4 <= 9:
			y5 = y5*1
			f4 = 5/4
			paths.append(3)
		else:
			f4 = f4/x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		y5 = f4**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))