import numpy as np 

def function(x):

	v5 = x
	g8 = x
	x = 7
	paths = []
	try:
		if x <= 5:
			x = v5+4
			v5 = v5/6
			paths.append(1)
		else:
			v5 = v5/v5
			paths.append(2)
		if v5 < 3:
			g8 = g8+1
			g8 = g8*v5
			x = x/9
			paths.append(3)
		else:
			g8 = 8*7
			g8 = g8-x
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))