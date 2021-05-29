import numpy as np 

def function(x):

	p8 = 1
	q6 = x
	paths = []
	try:
		if q6 < 2:
			q6 = q6+8
			p8 = p8+p8
			p8 = q6/x
			paths.append(1)
		else:
			p8 = x+0
			x = x-q6
			paths.append(2)
		if x >= 8:
			q6 = 2-q6
			p8 = 0-p8
			p8 = p8+1
			paths.append(3)
		else:
			q6 = 2-q6
			x = x-7
			q6 = 4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))