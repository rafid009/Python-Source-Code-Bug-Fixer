import numpy as np 

def function(x):

	w6 = x
	g2 = x
	paths = []
	try:
		if w6 >= 7:
			x = 0*8
			w6 = 9/1
			x = x+8
			paths.append(1)
		else:
			w6 = w6/1
			paths.append(2)
		if x > 4:
			g2 = g2*3
			w6 = 5/w6
			paths.append(3)
		else:
			x = x+w6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))