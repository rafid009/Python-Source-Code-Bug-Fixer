import numpy as np 

def function(x):

	g2 = 5
	o5 = x
	paths = []
	try:
		if g2 < 2:
			o5 = 3/o5
			g2 = g2+2
			paths.append(1)
		else:
			x = x-0
			g2 = g2*9
			paths.append(2)
		if x <= 4:
			o5 = 3-o5
			g2 = 3+g2
			paths.append(3)
		else:
			g2 = 1+g2
			g2 = g2-0
			o5 = o5+g2
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		o5 = o5**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))