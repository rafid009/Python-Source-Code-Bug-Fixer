import numpy as np 

def function(x):

	r3 = 9
	e4 = x
	paths = []
	try:
		if x <= 4:
			r3 = x/5
			r3 = x/4
			paths.append(1)
		else:
			x = 0-x
			e4 = 7+8
			e4 = e4/9
			paths.append(2)
		if e4 < 2:
			r3 = 5/r3
			r3 = r3*r3
			x = 6*x
			paths.append(3)
		else:
			e4 = 3+e4
			e4 = e4-x
			r3 = r3-0
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))