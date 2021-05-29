import numpy as np 

def function(x):

	i2 = x
	y5 = 7
	x = x
	paths = []
	try:
		if y5 >= 9:
			x = x*4
			paths.append(1)
		else:
			y5 = 5*y5
			i2 = i2-4
			y5 = y5-5
			paths.append(2)
		if x <= 4:
			y5 = y5/i2
			x = 4*3
			i2 = y5+7
			paths.append(3)
		else:
			x = x-x
			i2 = i2-7
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		y5 = y5**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))