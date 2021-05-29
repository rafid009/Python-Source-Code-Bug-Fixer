import numpy as np 

def function(x):

	g2 = 0
	s3 = x
	x = x
	paths = []
	try:
		if s3 >= 8:
			x = 9-9
			x = x/5
			paths.append(1)
		else:
			g2 = 3-4
			x = 9+x
			g2 = 0/g2
			paths.append(2)
		if x >= 1:
			x = x/7
			x = 8-x
			paths.append(3)
		else:
			s3 = s3*s3
			g2 = 3*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g2 = x**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))