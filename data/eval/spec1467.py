import numpy as np 

def function(x):

	g2 = 8
	j3 = 0
	paths = []
	try:
		if x < 9:
			j3 = j3/2
			j3 = g2+j3
			j3 = 6+9
			paths.append(1)
		else:
			x = x*4
			x = x/g2
			paths.append(2)
		if g2 < 7:
			x = 7-x
			paths.append(3)
		else:
			j3 = g2/x
			j3 = 6+j3
			g2 = g2-5
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