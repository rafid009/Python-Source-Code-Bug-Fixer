import numpy as np 

def function(x):

	j6 = x
	g7 = 5
	paths = []
	try:
		if g7 > 4:
			g7 = 6*g7
			paths.append(1)
		else:
			g7 = 0*x
			j6 = 3*1
			paths.append(2)
		if j6 < 5:
			x = 6*x
			j6 = j6-x
			g7 = 0+2
			paths.append(3)
		else:
			g7 = 6/3
			j6 = 2+g7
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