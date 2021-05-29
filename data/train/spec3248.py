import numpy as np 

def function(x):

	y5 = x
	a8 = x
	paths = []
	try:
		if y5 < 3:
			a8 = a8+5
			x = 2-2
			x = x*1
			paths.append(1)
		else:
			x = 3/2
			a8 = a8+2
			a8 = a8+4
			paths.append(2)
		if a8 < 4:
			x = 6/a8
			x = 8*8
			y5 = y5+0
			paths.append(3)
		else:
			y5 = 0/y5
			y5 = 4/a8
			y5 = 7-7
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		y5 = a8**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))