import numpy as np 

def function(x):

	d2 = x
	g5 = 5
	paths = []
	try:
		if g5 <= 6:
			g5 = 6-g5
			d2 = 1+d2
			d2 = d2/8
			paths.append(1)
		else:
			d2 = 0*8
			paths.append(2)
		if x > 1:
			x = x-0
			d2 = d2-7
			g5 = 8/x
			paths.append(3)
		else:
			g5 = g5*1
			g5 = g5+4
			g5 = d2-g5
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))