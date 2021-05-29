import numpy as np 

def function(x):

	g8 = 1
	o6 = x
	paths = []
	try:
		if x > 1:
			x = 4+g8
			x = x+2
			paths.append(1)
		else:
			g8 = g8-0
			paths.append(2)
		if x <= 4:
			o6 = o6*g8
			paths.append(3)
		else:
			o6 = o6-o6
			g8 = 8/6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))