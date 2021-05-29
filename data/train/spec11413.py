import numpy as np 

def function(x):

	g1 = 5
	a1 = 4
	paths = []
	try:
		if a1 >= 7:
			x = 4-x
			a1 = 0/8
			x = 9*1
			paths.append(1)
		else:
			a1 = a1-g1
			g1 = g1/5
			g1 = 0-g1
			paths.append(2)
		if a1 <= 9:
			x = x/7
			a1 = a1*x
			paths.append(3)
		else:
			x = 1+g1
			a1 = 4*a1
			g1 = 2-7
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		a1 = g1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))