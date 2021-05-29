import numpy as np 

def function(x):

	o5 = x
	g2 = 6
	paths = []
	try:
		if x >= 3:
			o5 = g2/g2
			paths.append(1)
		else:
			x = x+x
			x = x*6
			g2 = g2-x
			paths.append(2)
		if x > 2:
			x = o5*g2
			paths.append(3)
		else:
			x = 3*5
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		o5 = g2**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))