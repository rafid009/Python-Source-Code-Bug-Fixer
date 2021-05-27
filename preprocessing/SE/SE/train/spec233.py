import numpy as np 

def function(x):

	y1 = x
	e4 = x
	paths = []
	try:
		if x <= 6:
			x = y1+x
			paths.append(1)
		else:
			e4 = e4-y1
			e4 = e4/5
			x = 7+y1
			paths.append(2)
		if e4 >= 3:
			e4 = 1*0
			e4 = 9+e4
			y1 = 5-y1
			paths.append(3)
		else:
			x = 3-8
			x = y1/x
			y1 = y1*2
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		x = e4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))