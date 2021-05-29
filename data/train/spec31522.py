import numpy as np 

def function(x):

	y2 = 5
	i2 = x
	paths = []
	try:
		if i2 < 4:
			i2 = 5+y2
			paths.append(1)
		else:
			x = 7/7
			paths.append(2)
		if x <= 8:
			y2 = y2-6
			i2 = i2-6
			y2 = x*y2
			paths.append(3)
		else:
			x = y2+2
			x = 6+y2
			x = x-1
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))