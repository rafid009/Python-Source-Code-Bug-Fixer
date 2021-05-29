import numpy as np 

def function(x):

	a1 = 1
	g1 = x
	paths = []
	try:
		if x < 7:
			a1 = 4/5
			a1 = a1-9
			paths.append(1)
		else:
			x = 5*2
			paths.append(2)
		if a1 <= 9:
			g1 = 4-9
			paths.append(3)
		else:
			x = x/1
			g1 = 4-x
			a1 = a1/a1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))