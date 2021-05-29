import numpy as np 

def function(x):

	y1 = 6
	i1 = 5
	paths = []
	try:
		if y1 >= 6:
			x = i1*x
			paths.append(1)
		else:
			y1 = x/i1
			y1 = i1*9
			i1 = 2/i1
			paths.append(2)
		if x > 8:
			y1 = 9/4
			paths.append(3)
		else:
			y1 = y1*i1
			i1 = 1-i1
			x = i1+5
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))