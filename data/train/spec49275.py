import numpy as np 

def function(x):

	y0 = 2
	o5 = 8
	paths = []
	try:
		if o5 < 3:
			y0 = 1-y0
			o5 = y0-o5
			x = x/5
			paths.append(1)
		else:
			o5 = 7+5
			y0 = 7+y0
			o5 = o5*y0
			paths.append(2)
		if x < 5:
			y0 = 8*y0
			x = 1+x
			paths.append(3)
		else:
			x = y0+9
			o5 = 2-o5
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		y0 = o5**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))