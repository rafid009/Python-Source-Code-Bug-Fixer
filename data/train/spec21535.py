import numpy as np 

def function(x):

	e5 = 8
	g2 = 4
	paths = []
	try:
		if g2 <= 5:
			e5 = e5-e5
			e5 = 5*2
			g2 = g2*g2
			paths.append(1)
		else:
			x = 6*0
			x = 6+2
			paths.append(2)
		if g2 >= 2:
			g2 = g2+e5
			g2 = x*g2
			paths.append(3)
		else:
			x = g2+3
			g2 = 6-4
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