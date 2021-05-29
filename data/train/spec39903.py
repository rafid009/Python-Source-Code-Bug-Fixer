import numpy as np 

def function(x):

	g6 = x
	f4 = 6
	x = x
	paths = []
	try:
		if x <= 1:
			f4 = 4+9
			g6 = g6-9
			paths.append(1)
		else:
			f4 = 5/6
			x = 3*3
			f4 = f4/1
			paths.append(2)
		if x < 9:
			g6 = g6+6
			paths.append(3)
		else:
			x = x-9
			x = 1*8
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))