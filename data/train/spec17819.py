import numpy as np 

def function(x):

	o6 = x
	g2 = 8
	paths = []
	try:
		if g2 < 0:
			o6 = 0+1
			x = 9/4
			g2 = 1+4
			paths.append(1)
		else:
			g2 = 3+4
			paths.append(2)
		if g2 < 6:
			o6 = 2/5
			o6 = o6+3
			paths.append(3)
		else:
			x = 5*6
			x = o6/6
			o6 = 2-g2
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