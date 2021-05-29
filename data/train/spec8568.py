import numpy as np 

def function(x):

	g9 = 4
	x4 = 1
	paths = []
	try:
		if x4 <= 3:
			g9 = 5/g9
			g9 = x*8
			g9 = 5-g9
			paths.append(1)
		else:
			x4 = 3-x4
			x = x+x
			x4 = x*5
			paths.append(2)
		if g9 > 3:
			x = 6+x
			paths.append(3)
		else:
			x4 = x4+g9
			x4 = g9+0
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x4 = g9**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))