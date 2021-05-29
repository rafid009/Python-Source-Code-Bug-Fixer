import numpy as np 

def function(x):

	o4 = x
	y3 = 2
	paths = []
	try:
		if y3 > 1:
			o4 = 8/o4
			y3 = y3*7
			o4 = x*7
			paths.append(1)
		else:
			o4 = 7*5
			o4 = o4+2
			x = x*2
			paths.append(2)
		if o4 >= 7:
			o4 = 6*6
			y3 = 1-y3
			y3 = x+y3
			paths.append(3)
		else:
			o4 = o4*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))