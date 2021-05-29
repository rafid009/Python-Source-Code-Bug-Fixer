import numpy as np 

def function(x):

	e3 = x
	y1 = 5
	paths = []
	try:
		if y1 <= 8:
			x = x/6
			x = 8*y1
			paths.append(1)
		else:
			y1 = 8*6
			e3 = e3+7
			y1 = y1*8
			paths.append(2)
		if e3 > 7:
			e3 = e3+e3
			e3 = e3+x
			y1 = 7/y1
			paths.append(3)
		else:
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		y1 = e3**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))