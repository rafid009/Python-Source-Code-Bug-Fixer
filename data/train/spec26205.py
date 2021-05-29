import numpy as np 

def function(x):

	y1 = 5
	o7 = x
	x = x
	paths = []
	try:
		if y1 > 1:
			o7 = o7+8
			paths.append(1)
		else:
			x = x*0
			y1 = 1+8
			o7 = 8/5
			paths.append(2)
		if o7 >= 5:
			x = 9+y1
			o7 = 2*o7
			paths.append(3)
		else:
			o7 = o7*y1
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		y1 = o7**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))