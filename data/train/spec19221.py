import numpy as np 

def function(x):

	i0 = x
	g2 = x
	paths = []
	try:
		if x <= 6:
			g2 = g2+4
			i0 = i0-i0
			paths.append(1)
		else:
			i0 = 7+9
			x = g2+x
			i0 = i0*1
			paths.append(2)
		if i0 < 8:
			x = x-5
			x = 4*x
			paths.append(3)
		else:
			g2 = 5-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))