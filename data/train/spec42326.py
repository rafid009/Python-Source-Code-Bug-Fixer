import numpy as np 

def function(x):

	y4 = x
	v5 = 5
	x = 6
	paths = []
	try:
		if v5 < 6:
			v5 = y4/7
			y4 = y4*9
			paths.append(1)
		else:
			v5 = v5-v5
			paths.append(2)
		if x > 5:
			v5 = 1+5
			x = x-4
			paths.append(3)
		else:
			v5 = 5/v5
			x = 3-5
			y4 = y4+x
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