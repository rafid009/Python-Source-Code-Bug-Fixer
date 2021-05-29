import numpy as np 

def function(x):

	e7 = x
	p6 = 7
	paths = []
	try:
		if e7 >= 7:
			e7 = e7-7
			p6 = p6-8
			paths.append(1)
		else:
			e7 = 2+e7
			x = p6/x
			paths.append(2)
		if p6 > 2:
			x = x+4
			x = x-x
			e7 = e7/2
			paths.append(3)
		else:
			e7 = p6-7
			p6 = p6+e7
			p6 = e7*8
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))