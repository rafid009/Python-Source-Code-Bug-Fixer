import numpy as np 

def function(x):

	g2 = 6
	v3 = 3
	paths = []
	try:
		if v3 <= 0:
			x = x-g2
			v3 = 0/g2
			paths.append(1)
		else:
			g2 = g2-3
			g2 = g2*8
			paths.append(2)
		if v3 < 4:
			v3 = v3*x
			paths.append(3)
		else:
			g2 = 0-g2
			g2 = g2/v3
			v3 = v3*2
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))