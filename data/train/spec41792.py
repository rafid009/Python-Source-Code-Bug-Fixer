import numpy as np 

def function(x):

	g2 = 9
	d1 = x
	paths = []
	try:
		if d1 <= 5:
			g2 = 4*d1
			paths.append(1)
		else:
			x = 7/x
			g2 = g2-g2
			paths.append(2)
		if d1 >= 1:
			d1 = d1+8
			x = 1+3
			g2 = g2*x
			paths.append(3)
		else:
			d1 = 0*0
			x = x+2
			x = x*7
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		d1 = g2**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))