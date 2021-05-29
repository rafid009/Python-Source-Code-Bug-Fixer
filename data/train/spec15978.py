import numpy as np 

def function(x):

	y5 = 3
	o8 = x
	paths = []
	try:
		if x > 6:
			y5 = y5-9
			paths.append(1)
		else:
			o8 = o8*9
			y5 = y5/7
			paths.append(2)
		if o8 <= 2:
			y5 = y5-3
			x = 9+x
			o8 = o8-5
			paths.append(3)
		else:
			y5 = y5*y5
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		y5 = o8**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))