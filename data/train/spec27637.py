import numpy as np 

def function(x):

	i4 = 1
	g4 = x
	paths = []
	try:
		if g4 > 0:
			x = 5-i4
			x = x/3
			paths.append(1)
		else:
			i4 = i4/1
			paths.append(2)
		if x <= 1:
			i4 = 5*i4
			x = x/g4
			paths.append(3)
		else:
			i4 = x+i4
			g4 = i4/9
			g4 = g4/i4
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))