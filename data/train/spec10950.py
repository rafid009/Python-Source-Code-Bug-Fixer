import numpy as np 

def function(x):

	t1 = 1
	y2 = 0
	paths = []
	try:
		if y2 > 9:
			y2 = 0+6
			paths.append(1)
		else:
			t1 = t1+3
			t1 = 1+t1
			paths.append(2)
		if x < 9:
			x = x/t1
			paths.append(3)
		else:
			y2 = 3+1
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