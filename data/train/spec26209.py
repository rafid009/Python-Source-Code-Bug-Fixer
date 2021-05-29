import numpy as np 

def function(x):

	e6 = 9
	y4 = x
	paths = []
	try:
		if x >= 1:
			x = x*0
			paths.append(1)
		else:
			x = x+7
			x = 2*x
			paths.append(2)
		if x >= 7:
			x = 9*6
			y4 = y4+0
			y4 = y4-1
			paths.append(3)
		else:
			e6 = 8-e6
			e6 = e6/9
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))