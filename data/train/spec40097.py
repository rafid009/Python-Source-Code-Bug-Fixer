import numpy as np 

def function(x):

	e8 = x
	g3 = x
	x = x
	paths = []
	try:
		if x > 6:
			g3 = g3+8
			paths.append(1)
		else:
			g3 = e8*0
			x = x+9
			g3 = x/x
			paths.append(2)
		if g3 <= 0:
			g3 = g3-e8
			g3 = g3+8
			g3 = 5-g3
			paths.append(3)
		else:
			g3 = g3-e8
			g3 = 8/g3
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		e8 = g3**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))