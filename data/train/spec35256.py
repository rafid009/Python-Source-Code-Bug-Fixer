import numpy as np 

def function(x):

	e9 = x
	g2 = 6
	x = 4
	paths = []
	try:
		if g2 >= 4:
			x = 0+x
			paths.append(1)
		else:
			g2 = g2/1
			g2 = e9/g2
			x = g2/2
			paths.append(2)
		if e9 >= 8:
			x = x/x
			x = 4-8
			x = x*3
			paths.append(3)
		else:
			g2 = g2/9
			g2 = g2-8
			e9 = e9*8
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