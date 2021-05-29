import numpy as np 

def function(x):

	y4 = x
	x6 = x
	paths = []
	try:
		if y4 <= 8:
			x6 = x+x6
			x6 = y4+2
			paths.append(1)
		else:
			y4 = 5*3
			y4 = 7/y4
			y4 = 8-y4
			paths.append(2)
		if x6 > 9:
			x = x6*9
			x6 = y4-9
			y4 = y4/9
			paths.append(3)
		else:
			y4 = x-8
			y4 = x6*5
			x = x+9
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