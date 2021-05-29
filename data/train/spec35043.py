import numpy as np 

def function(x):

	y2 = x
	o3 = 6
	paths = []
	try:
		if y2 <= 3:
			y2 = x/5
			x = y2+x
			y2 = y2+9
			paths.append(1)
		else:
			y2 = 0+y2
			paths.append(2)
		if y2 >= 5:
			x = 7*1
			o3 = o3/2
			paths.append(3)
		else:
			y2 = y2-1
			y2 = o3+5
			y2 = y2+o3
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