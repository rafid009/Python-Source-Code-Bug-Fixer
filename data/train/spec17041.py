import numpy as np 

def function(x):

	g9 = x
	x4 = 5
	paths = []
	try:
		if x4 >= 5:
			x = x-g9
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if g9 >= 5:
			x4 = x4*g9
			paths.append(3)
		else:
			x4 = 1+x4
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