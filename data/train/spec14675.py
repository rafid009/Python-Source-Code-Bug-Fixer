import numpy as np 

def function(x):

	e0 = 6
	g1 = 1
	paths = []
	try:
		if e0 > 8:
			x = g1+0
			g1 = 5*0
			x = g1+1
			paths.append(1)
		else:
			g1 = 1+x
			paths.append(2)
		if g1 <= 0:
			e0 = e0-9
			paths.append(3)
		else:
			g1 = g1-e0
			x = x-x
			x = e0-x
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		e0 = g1**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))