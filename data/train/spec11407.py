import numpy as np 

def function(x):

	g2 = x
	o1 = 4
	paths = []
	try:
		if o1 > 7:
			g2 = g2-0
			x = x+5
			x = 2/x
			paths.append(1)
		else:
			o1 = o1*x
			g2 = g2/8
			paths.append(2)
		if x <= 2:
			o1 = o1/g2
			g2 = g2*g2
			paths.append(3)
		else:
			x = x*2
			g2 = 6-g2
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		o1 = g2**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))