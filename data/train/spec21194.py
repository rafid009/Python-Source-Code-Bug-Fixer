import numpy as np 

def function(x):

	y1 = x
	j6 = x
	paths = []
	try:
		if y1 > 7:
			x = j6/6
			j6 = j6+j6
			x = 5-x
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if x > 7:
			x = x*7
			paths.append(3)
		else:
			j6 = j6-2
			y1 = 9*y1
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))