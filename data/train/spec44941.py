import numpy as np 

def function(x):

	g3 = x
	e2 = 6
	paths = []
	try:
		if g3 <= 3:
			e2 = 1-e2
			x = 4/e2
			paths.append(1)
		else:
			g3 = x+g3
			e2 = g3/e2
			g3 = e2/x
			paths.append(2)
		if x <= 7:
			g3 = g3+9
			e2 = 3/x
			paths.append(3)
		else:
			e2 = 1*g3
			x = 5-9
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))