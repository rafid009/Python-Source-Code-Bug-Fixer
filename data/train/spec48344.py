import numpy as np 

def function(x):

	g3 = x
	a5 = 5
	x = x
	paths = []
	try:
		if a5 <= 9:
			a5 = 4-a5
			paths.append(1)
		else:
			g3 = a5*3
			paths.append(2)
		if g3 >= 5:
			g3 = x+7
			a5 = x/x
			a5 = 7/x
			paths.append(3)
		else:
			g3 = g3+7
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))