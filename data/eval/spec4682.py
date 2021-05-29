import numpy as np 

def function(x):

	a8 = 4
	g9 = x
	paths = []
	try:
		if x <= 8:
			x = 5+3
			x = 8-a8
			paths.append(1)
		else:
			a8 = a8/x
			paths.append(2)
		if g9 <= 3:
			x = a8-x
			x = 4+a8
			paths.append(3)
		else:
			a8 = a8+x
			a8 = a8*a8
			a8 = 7*8
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