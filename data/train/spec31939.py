import numpy as np 

def function(x):

	u8 = x
	j8 = 4
	paths = []
	try:
		if x <= 8:
			j8 = j8+3
			u8 = 5/u8
			u8 = u8+1
			paths.append(1)
		else:
			j8 = j8*5
			paths.append(2)
		if j8 <= 0:
			x = 7*x
			j8 = u8*j8
			j8 = 8-3
			paths.append(3)
		else:
			u8 = x-u8
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