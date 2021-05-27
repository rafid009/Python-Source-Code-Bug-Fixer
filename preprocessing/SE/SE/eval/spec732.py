import numpy as np 

def function(x):

	g2 = 0
	o9 = 4
	x = x
	paths = []
	try:
		if o9 >= 1:
			o9 = 4-o9
			g2 = g2*g2
			paths.append(1)
		else:
			o9 = 4+0
			o9 = x-1
			o9 = g2*x
			paths.append(2)
		if x <= 4:
			x = x+o9
			paths.append(3)
		else:
			o9 = 5-o9
			g2 = 1+1
			g2 = g2/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))