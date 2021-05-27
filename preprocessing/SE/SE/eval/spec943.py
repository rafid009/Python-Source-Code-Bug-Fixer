import numpy as np 

def function(x):

	o1 = x
	g8 = x
	paths = []
	try:
		if g8 > 2:
			x = x/4
			g8 = 8+5
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if o1 >= 9:
			g8 = 4/g8
			g8 = 7*g8
			paths.append(3)
		else:
			o1 = g8/x
			o1 = o1*3
			x = 8+4
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		o1 = g8**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))