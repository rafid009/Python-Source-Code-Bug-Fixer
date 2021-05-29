import numpy as np 

def function(x):

	e1 = x
	r7 = 6
	paths = []
	try:
		if r7 < 7:
			x = 2/x
			r7 = 1-x
			paths.append(1)
		else:
			e1 = 5+3
			paths.append(2)
		if r7 < 8:
			e1 = 6+e1
			e1 = e1/1
			paths.append(3)
		else:
			e1 = 8*1
			x = x*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))