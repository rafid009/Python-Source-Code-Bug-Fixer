import numpy as np 

def function(x):

	i5 = x
	y3 = x
	x = x
	paths = []
	try:
		if x <= 3:
			i5 = i5-7
			paths.append(1)
		else:
			x = x-i5
			i5 = 9-i5
			paths.append(2)
		if y3 >= 4:
			y3 = 4/y3
			y3 = 0+y3
			i5 = i5+1
			paths.append(3)
		else:
			y3 = y3+7
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