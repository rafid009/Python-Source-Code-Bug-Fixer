import numpy as np 

def function(x):

	i2 = 2
	v6 = 3
	paths = []
	try:
		if v6 >= 0:
			i2 = i2/v6
			paths.append(1)
		else:
			v6 = 8+x
			x = x*5
			v6 = v6/i2
			paths.append(2)
		if x > 7:
			x = x/x
			v6 = v6/x
			x = 3+7
			paths.append(3)
		else:
			v6 = 2-v6
			i2 = x*3
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