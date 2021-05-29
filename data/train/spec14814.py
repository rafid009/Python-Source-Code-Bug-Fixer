import numpy as np 

def function(x):

	d5 = 4
	y6 = 4
	x = 7
	paths = []
	try:
		if y6 <= 1:
			y6 = y6-y6
			paths.append(1)
		else:
			d5 = d5+1
			x = x+7
			d5 = y6*2
			paths.append(2)
		if x < 6:
			d5 = 7/d5
			paths.append(3)
		else:
			d5 = d5-x
			y6 = d5*y6
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		x = y6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))