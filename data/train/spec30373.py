import numpy as np 

def function(x):

	j9 = x
	g2 = x
	x = x
	paths = []
	try:
		if x <= 0:
			j9 = 2-j9
			paths.append(1)
		else:
			g2 = g2/5
			paths.append(2)
		if g2 < 0:
			g2 = 7+5
			j9 = 2/j9
			paths.append(3)
		else:
			g2 = g2-9
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