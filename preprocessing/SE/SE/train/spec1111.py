import numpy as np 

def function(x):

	g6 = x
	o4 = x
	paths = []
	try:
		if g6 > 6:
			x = 2*x
			o4 = o4/5
			x = o4/x
			paths.append(1)
		else:
			x = 2+7
			g6 = o4*0
			g6 = g6+o4
			paths.append(2)
		if o4 >= 9:
			o4 = x+4
			g6 = 2/g6
			o4 = 7/o4
			paths.append(3)
		else:
			o4 = x+o4
			x = x+3
			x = x/9
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))