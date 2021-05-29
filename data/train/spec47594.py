import numpy as np 

def function(x):

	g5 = x
	o6 = 7
	paths = []
	try:
		if x >= 5:
			g5 = 1-g5
			x = x*7
			g5 = g5-o6
			paths.append(1)
		else:
			x = 5-o6
			g5 = g5/7
			g5 = g5+5
			paths.append(2)
		if x < 6:
			o6 = o6/5
			o6 = o6/7
			x = 4-3
			paths.append(3)
		else:
			o6 = 4*1
			x = 4+x
			o6 = 2-o6
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