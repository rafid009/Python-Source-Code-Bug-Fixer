import numpy as np 

def function(x):

	e2 = x
	y0 = 6
	paths = []
	try:
		if e2 > 5:
			x = e2+y0
			y0 = y0+9
			paths.append(1)
		else:
			y0 = y0*8
			y0 = y0*e2
			x = x+3
			paths.append(2)
		if e2 < 0:
			e2 = 4+7
			y0 = y0+e2
			x = x+6
			paths.append(3)
		else:
			y0 = y0+y0
			y0 = y0/1
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		y0 = y0**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))