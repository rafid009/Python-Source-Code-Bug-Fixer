import numpy as np 

def function(x):

	s5 = 2
	g2 = x
	paths = []
	try:
		if g2 < 5:
			g2 = g2-g2
			x = 5-4
			paths.append(1)
		else:
			x = 5-x
			x = 9/x
			paths.append(2)
		if x < 5:
			g2 = g2/9
			x = 2+x
			s5 = g2*s5
			paths.append(3)
		else:
			s5 = 5*s5
			s5 = s5/x
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))