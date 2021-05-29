import numpy as np 

def function(x):

	g0 = x
	y4 = 9
	paths = []
	try:
		if y4 <= 4:
			x = x+0
			y4 = x-g0
			x = x+1
			paths.append(1)
		else:
			x = x*6
			x = x-2
			paths.append(2)
		if y4 > 7:
			y4 = 6-y4
			y4 = 7/y4
			x = x-x
			paths.append(3)
		else:
			x = x-9
			g0 = y4/g0
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		y4 = g0**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))