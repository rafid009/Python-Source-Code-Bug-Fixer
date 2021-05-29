import numpy as np 

def function(x):

	l4 = x
	g2 = 7
	paths = []
	try:
		if l4 > 4:
			l4 = l4/8
			paths.append(1)
		else:
			g2 = g2-3
			g2 = 0+4
			g2 = x*x
			paths.append(2)
		if g2 >= 4:
			l4 = l4-9
			g2 = l4+g2
			paths.append(3)
		else:
			x = 6-6
			x = x/2
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		l4 = g2**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))