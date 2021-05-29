import numpy as np 

def function(x):

	v9 = 7
	g9 = 8
	paths = []
	try:
		if v9 >= 0:
			v9 = v9-x
			g9 = 9+3
			x = x*2
			paths.append(1)
		else:
			v9 = v9-2
			paths.append(2)
		if g9 <= 9:
			g9 = g9+6
			v9 = 7-8
			paths.append(3)
		else:
			g9 = x-4
			x = x-v9
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))