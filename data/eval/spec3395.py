import numpy as np 

def function(x):

	g6 = x
	f8 = 1
	paths = []
	try:
		if f8 >= 5:
			x = 3+f8
			g6 = x+x
			f8 = 3*0
			paths.append(1)
		else:
			g6 = 7-0
			paths.append(2)
		if g6 > 4:
			f8 = f8-0
			g6 = g6-x
			x = g6/x
			paths.append(3)
		else:
			x = x/x
			x = x+6
			f8 = f8-7
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))