import numpy as np 

def function(x):

	o2 = x
	g7 = 1
	paths = []
	try:
		if x < 4:
			x = o2+x
			paths.append(1)
		else:
			o2 = 1-7
			g7 = g7/o2
			paths.append(2)
		if o2 < 9:
			x = 5-x
			paths.append(3)
		else:
			g7 = g7-1
			x = x*1
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))