import numpy as np 

def function(x):

	i2 = x
	k4 = x
	paths = []
	try:
		if x < 2:
			x = 5+x
			x = x*5
			i2 = i2/8
			paths.append(1)
		else:
			x = 6+x
			i2 = i2/3
			paths.append(2)
		if x > 3:
			i2 = 3+0
			paths.append(3)
		else:
			k4 = i2-k4
			i2 = 5/x
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		k4 = k4**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))