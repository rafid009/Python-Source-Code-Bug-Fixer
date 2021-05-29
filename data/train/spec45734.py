import numpy as np 

def function(x):

	i2 = 4
	e8 = x
	paths = []
	try:
		if i2 > 6:
			x = x/x
			paths.append(1)
		else:
			i2 = e8/i2
			i2 = e8-3
			x = x+1
			paths.append(2)
		if i2 < 6:
			i2 = x+i2
			paths.append(3)
		else:
			i2 = 6+i2
			x = 6/x
			e8 = 9+2
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		i2 = e8**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))