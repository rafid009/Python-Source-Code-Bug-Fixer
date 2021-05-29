import numpy as np 

def function(x):

	g5 = 9
	e6 = x
	paths = []
	try:
		if e6 >= 7:
			g5 = 9+g5
			e6 = e6*1
			paths.append(1)
		else:
			e6 = 7*e6
			g5 = g5-3
			e6 = e6+1
			paths.append(2)
		if x >= 6:
			x = x+e6
			paths.append(3)
		else:
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))