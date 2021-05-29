import numpy as np 

def function(x):

	g8 = 4
	v3 = x
	paths = []
	try:
		if v3 <= 7:
			g8 = g8-v3
			x = 1+6
			v3 = x/v3
			paths.append(1)
		else:
			g8 = 7-x
			v3 = v3+8
			g8 = 5+x
			paths.append(2)
		if x <= 2:
			v3 = 4-3
			v3 = x*1
			paths.append(3)
		else:
			x = x-3
			v3 = 3/1
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