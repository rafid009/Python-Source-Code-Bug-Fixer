import numpy as np 

def function(x):

	i2 = x
	u4 = 9
	paths = []
	try:
		if i2 >= 1:
			i2 = 5-x
			u4 = 2-u4
			x = 3-2
			paths.append(1)
		else:
			i2 = 3+i2
			x = 9+x
			paths.append(2)
		if x < 0:
			u4 = 0/1
			i2 = i2*i2
			i2 = 5*i2
			paths.append(3)
		else:
			i2 = i2/i2
			i2 = i2-i2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))