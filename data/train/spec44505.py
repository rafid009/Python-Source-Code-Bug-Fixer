import numpy as np 

def function(x):

	e2 = 9
	g9 = 2
	paths = []
	try:
		if e2 < 0:
			e2 = e2*3
			e2 = 6/e2
			g9 = 0+g9
			paths.append(1)
		else:
			g9 = 0+x
			paths.append(2)
		if e2 > 2:
			e2 = e2-e2
			g9 = x*1
			paths.append(3)
		else:
			x = e2-2
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		e2 = g9**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))