import numpy as np 

def function(x):

	g9 = 9
	i7 = x
	paths = []
	try:
		if i7 <= 4:
			i7 = i7+6
			paths.append(1)
		else:
			g9 = i7+8
			g9 = i7*7
			paths.append(2)
		if g9 > 9:
			g9 = g9+3
			x = 0/x
			paths.append(3)
		else:
			g9 = i7*7
			i7 = i7-4
			x = i7/5
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