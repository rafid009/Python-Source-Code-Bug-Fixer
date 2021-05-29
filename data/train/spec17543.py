import numpy as np 

def function(x):

	e2 = x
	y3 = 8
	paths = []
	try:
		if e2 <= 4:
			x = 4+4
			paths.append(1)
		else:
			y3 = x/1
			e2 = 4+e2
			paths.append(2)
		if x <= 7:
			y3 = 0-3
			e2 = 9*x
			paths.append(3)
		else:
			x = 4+x
			x = x*4
			y3 = y3-5
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))