import numpy as np 

def function(x):

	g8 = 4
	i6 = x
	paths = []
	try:
		if g8 <= 9:
			g8 = g8*3
			x = x+3
			x = 9*1
			paths.append(1)
		else:
			x = x+6
			g8 = g8-4
			i6 = i6+0
			paths.append(2)
		if i6 <= 7:
			i6 = i6*1
			x = x/2
			paths.append(3)
		else:
			i6 = g8+7
			g8 = 5-x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		g8 = i6**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))