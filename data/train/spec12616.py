import numpy as np 

def function(x):

	y6 = x
	i5 = 5
	paths = []
	try:
		if y6 < 0:
			i5 = 7/4
			y6 = i5+y6
			x = 3*y6
			paths.append(1)
		else:
			y6 = y6*x
			x = 4/x
			x = x/1
			paths.append(2)
		if i5 < 7:
			y6 = 2/x
			x = 9*x
			paths.append(3)
		else:
			i5 = y6+5
			x = y6-x
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		i5 = y6**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))