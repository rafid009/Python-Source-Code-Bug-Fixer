import numpy as np 

def function(x):

	t9 = x
	y4 = x
	paths = []
	try:
		if x <= 9:
			x = x+2
			paths.append(1)
		else:
			y4 = y4-8
			paths.append(2)
		if y4 <= 0:
			x = x*x
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		y4 = t9**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))