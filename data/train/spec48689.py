import numpy as np 

def function(x):

	v4 = 4
	i2 = x
	paths = []
	try:
		if x >= 6:
			x = v4-1
			i2 = i2+3
			x = x+9
			paths.append(1)
		else:
			v4 = i2-9
			paths.append(2)
		if v4 > 5:
			v4 = 6/4
			i2 = 7+7
			paths.append(3)
		else:
			v4 = 7+3
			v4 = v4-3
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		x = i2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))