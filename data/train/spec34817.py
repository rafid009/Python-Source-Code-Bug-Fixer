import numpy as np 

def function(x):

	g2 = 7
	a2 = x
	paths = []
	try:
		if g2 < 8:
			g2 = g2-2
			a2 = a2/x
			x = g2+7
			paths.append(1)
		else:
			g2 = 8*g2
			g2 = a2+1
			x = 8-g2
			paths.append(2)
		if x < 5:
			x = x+1
			x = 5/x
			paths.append(3)
		else:
			x = g2+5
			x = 3+x
			a2 = a2-x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))