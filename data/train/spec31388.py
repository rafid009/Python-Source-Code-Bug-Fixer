import numpy as np 

def function(x):

	y2 = 7
	d5 = x
	paths = []
	try:
		if d5 >= 4:
			y2 = 1+7
			y2 = d5*3
			paths.append(1)
		else:
			y2 = x/y2
			y2 = y2/1
			x = x/1
			paths.append(2)
		if y2 <= 3:
			y2 = 1-d5
			y2 = 5/7
			paths.append(3)
		else:
			x = 6/4
			d5 = x/d5
			y2 = y2+7
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