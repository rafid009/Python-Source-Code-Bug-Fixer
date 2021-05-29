import numpy as np 

def function(x):

	p7 = x
	q8 = 4
	x = 2
	paths = []
	try:
		if q8 > 6:
			x = q8/x
			q8 = q8*8
			paths.append(1)
		else:
			x = x*p7
			x = x+8
			x = x*p7
			paths.append(2)
		if q8 <= 5:
			q8 = q8+p7
			paths.append(3)
		else:
			p7 = q8*8
			x = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))