import numpy as np 

def function(x):

	n4 = 7
	e8 = x
	paths = []
	try:
		if n4 < 5:
			x = 2+x
			x = 3-x
			paths.append(1)
		else:
			e8 = 2-1
			n4 = 6/4
			x = 6*x
			paths.append(2)
		if x > 4:
			e8 = 3-e8
			x = x+1
			paths.append(3)
		else:
			x = x+8
			n4 = e8*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))