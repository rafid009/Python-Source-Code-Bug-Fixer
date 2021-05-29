import numpy as np 

def function(x):

	g2 = 1
	o1 = x
	paths = []
	try:
		if g2 <= 2:
			o1 = 4+o1
			x = 9+5
			o1 = x/g2
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if o1 <= 7:
			g2 = x/o1
			paths.append(3)
		else:
			x = x-x
			g2 = g2-5
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		x = g2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))