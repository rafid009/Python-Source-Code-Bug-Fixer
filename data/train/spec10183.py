import numpy as np 

def function(x):

	e9 = x
	g4 = x
	paths = []
	try:
		if x > 8:
			x = x-1
			paths.append(1)
		else:
			g4 = 5-2
			x = x+e9
			x = 1+x
			paths.append(2)
		if g4 <= 4:
			g4 = g4*4
			g4 = 9/g4
			g4 = 6/9
			paths.append(3)
		else:
			g4 = 2-g4
			e9 = e9/e9
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		e9 = g4**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))