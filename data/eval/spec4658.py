import numpy as np 

def function(x):

	r3 = x
	y6 = 8
	x = 9
	paths = []
	try:
		if y6 <= 9:
			y6 = 4*9
			paths.append(1)
		else:
			x = 7-0
			y6 = y6/2
			paths.append(2)
		if r3 >= 0:
			r3 = y6-r3
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		y6 = r3**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))