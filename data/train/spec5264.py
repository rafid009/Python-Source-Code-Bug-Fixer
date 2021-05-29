import numpy as np 

def function(x):

	k1 = x
	y5 = x
	paths = []
	try:
		if y5 > 8:
			y5 = y5*9
			paths.append(1)
		else:
			k1 = 3+x
			paths.append(2)
		if x < 3:
			y5 = x/1
			y5 = 8+7
			paths.append(3)
		else:
			k1 = y5*3
			x = k1/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))