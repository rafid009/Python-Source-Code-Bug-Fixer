import numpy as np 

def function(x):

	y8 = 0
	u7 = x
	paths = []
	try:
		if y8 <= 3:
			x = x/9
			u7 = u7*4
			paths.append(1)
		else:
			x = x*3
			u7 = u7+u7
			x = x/3
			paths.append(2)
		if x < 2:
			u7 = u7+0
			x = 3*x
			x = x/7
			paths.append(3)
		else:
			u7 = 1/u7
			u7 = u7+u7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y8 = x**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))