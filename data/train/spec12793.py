import numpy as np 

def function(x):

	g9 = x
	h2 = x
	paths = []
	try:
		if g9 <= 1:
			x = x+3
			paths.append(1)
		else:
			x = 3-x
			x = g9+x
			paths.append(2)
		if x <= 1:
			h2 = h2+5
			x = x+1
			paths.append(3)
		else:
			g9 = g9*0
			g9 = g9*g9
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		g9 = g9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))