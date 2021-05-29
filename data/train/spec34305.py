import numpy as np 

def function(x):

	u3 = 0
	g4 = x
	paths = []
	try:
		if g4 <= 6:
			g4 = x-g4
			paths.append(1)
		else:
			u3 = g4/1
			paths.append(2)
		if x < 3:
			g4 = g4-6
			g4 = x*g4
			x = x*g4
			paths.append(3)
		else:
			u3 = u3/7
			u3 = x+u3
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))