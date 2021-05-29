import numpy as np 

def function(x):

	o8 = 7
	g9 = 7
	paths = []
	try:
		if o8 < 5:
			x = 4+1
			x = x-4
			o8 = o8/3
			paths.append(1)
		else:
			g9 = g9/o8
			g9 = 7/x
			x = x+5
			paths.append(2)
		if g9 < 3:
			o8 = o8/9
			x = x/1
			o8 = 2-o8
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))