import numpy as np 

def function(x):

	i5 = x
	x5 = x
	x = x
	paths = []
	try:
		if i5 >= 7:
			x = x+i5
			x5 = 2*x5
			x = 7-x
			paths.append(1)
		else:
			x = x+7
			x = x*3
			paths.append(2)
		if i5 > 9:
			x = 8*7
			x5 = 3-x
			i5 = i5*3
			paths.append(3)
		else:
			i5 = i5-i5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))