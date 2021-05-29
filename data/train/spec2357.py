import numpy as np 

def function(x):

	b6 = x
	o7 = x
	x = 3
	paths = []
	try:
		if x >= 2:
			x = b6*b6
			paths.append(1)
		else:
			x = 4*5
			b6 = x+b6
			paths.append(2)
		if x < 4:
			b6 = 1*b6
			x = x/3
			paths.append(3)
		else:
			b6 = 9/3
			x = b6*3
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))