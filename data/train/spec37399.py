import numpy as np 

def function(x):

	e2 = 5
	g5 = x
	paths = []
	try:
		if g5 <= 3:
			x = 4+x
			e2 = e2-5
			paths.append(1)
		else:
			e2 = e2+9
			paths.append(2)
		if x <= 8:
			x = x+e2
			paths.append(3)
		else:
			e2 = 7*3
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))