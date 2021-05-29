import numpy as np 

def function(x):

	y7 = 2
	v1 = 8
	paths = []
	try:
		if x > 6:
			x = x+5
			paths.append(1)
		else:
			y7 = y7/9
			y7 = y7/9
			x = x/3
			paths.append(2)
		if v1 >= 4:
			y7 = y7-y7
			y7 = 7*1
			y7 = v1+0
			paths.append(3)
		else:
			x = x*7
			y7 = v1-y7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))