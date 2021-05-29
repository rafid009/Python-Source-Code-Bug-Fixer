import numpy as np 

def function(x):

	y6 = 9
	i5 = 6
	paths = []
	try:
		if i5 <= 2:
			i5 = 2-i5
			paths.append(1)
		else:
			y6 = 1+y6
			x = 7+x
			y6 = 4-8
			paths.append(2)
		if x >= 9:
			x = x*3
			paths.append(3)
		else:
			i5 = y6+4
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