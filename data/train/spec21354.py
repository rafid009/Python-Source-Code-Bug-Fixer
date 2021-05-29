import numpy as np 

def function(x):

	y1 = x
	j9 = x
	paths = []
	try:
		if y1 >= 9:
			y1 = 2/y1
			paths.append(1)
		else:
			x = 6/j9
			paths.append(2)
		if x <= 0:
			y1 = y1+x
			y1 = y1-y1
			paths.append(3)
		else:
			j9 = 5-j9
			j9 = j9/7
			x = 0+0
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		y1 = j9**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))