import numpy as np 

def function(x):

	g7 = x
	f7 = 3
	paths = []
	try:
		if x <= 2:
			x = g7-8
			f7 = 5*g7
			x = 7*x
			paths.append(1)
		else:
			f7 = 9+1
			f7 = x+7
			f7 = 7+0
			paths.append(2)
		if g7 <= 8:
			g7 = 5*g7
			f7 = x/6
			paths.append(3)
		else:
			x = g7+5
			x = 6/6
			f7 = 9-g7
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		f7 = g7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))