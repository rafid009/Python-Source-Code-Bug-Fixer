import numpy as np 

def function(x):

	u8 = x
	g9 = x
	paths = []
	try:
		if u8 <= 2:
			u8 = g9*4
			paths.append(1)
		else:
			x = 4-g9
			paths.append(2)
		if g9 >= 9:
			g9 = g9+5
			x = u8+3
			g9 = g9+9
			paths.append(3)
		else:
			g9 = u8-g9
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