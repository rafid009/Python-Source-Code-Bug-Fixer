import numpy as np 

def function(x):

	y2 = 3
	e0 = x
	paths = []
	try:
		if e0 <= 1:
			y2 = x*y2
			y2 = e0/9
			paths.append(1)
		else:
			y2 = y2+e0
			y2 = e0*x
			y2 = y2+0
			paths.append(2)
		if y2 >= 7:
			y2 = y2-5
			e0 = e0-2
			paths.append(3)
		else:
			e0 = e0+x
			y2 = 1/2
			x = x/e0
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))