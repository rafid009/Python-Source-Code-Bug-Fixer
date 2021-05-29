import numpy as np 

def function(x):

	e4 = 5
	x2 = 7
	x = x
	paths = []
	try:
		if x2 <= 3:
			x = x+e4
			x = 2*x
			paths.append(1)
		else:
			e4 = x*8
			e4 = 0+x
			e4 = 8*0
			paths.append(2)
		if x2 > 0:
			e4 = 5-7
			x = 3/8
			paths.append(3)
		else:
			x = 7/4
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