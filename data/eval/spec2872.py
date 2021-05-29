import numpy as np 

def function(x):

	g2 = x
	o0 = x
	paths = []
	try:
		if o0 >= 8:
			x = x+x
			g2 = 5*g2
			o0 = o0+9
			paths.append(1)
		else:
			o0 = o0/4
			x = 2*x
			x = x/1
			paths.append(2)
		if o0 < 6:
			x = 7/x
			g2 = g2+g2
			paths.append(3)
		else:
			g2 = 2-g2
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		g2 = o0**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))