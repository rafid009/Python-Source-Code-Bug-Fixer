import numpy as np 

def function(x):

	y4 = 9
	b0 = 4
	paths = []
	try:
		if x > 2:
			b0 = 9/b0
			paths.append(1)
		else:
			y4 = y4-5
			paths.append(2)
		if b0 <= 5:
			y4 = 3-y4
			paths.append(3)
		else:
			b0 = b0+7
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))