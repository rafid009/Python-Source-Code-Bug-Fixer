import numpy as np 

def function(x):

	i2 = x
	y0 = x
	paths = []
	try:
		if x < 4:
			x = x*6
			y0 = y0*i2
			paths.append(1)
		else:
			i2 = i2-7
			x = x+9
			paths.append(2)
		if y0 <= 0:
			x = 8*5
			y0 = y0*2
			paths.append(3)
		else:
			i2 = 7*i2
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		y0 = i2**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))