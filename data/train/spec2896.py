import numpy as np 

def function(x):

	y1 = 1
	o2 = 3
	paths = []
	try:
		if x < 3:
			o2 = 3/o2
			paths.append(1)
		else:
			o2 = 3*o2
			paths.append(2)
		if o2 <= 7:
			o2 = o2-1
			y1 = 5*y1
			paths.append(3)
		else:
			o2 = o2+1
			o2 = y1-o2
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