import numpy as np 

def function(x):

	q4 = x
	p8 = 4
	paths = []
	try:
		if x < 2:
			q4 = p8*x
			q4 = q4*p8
			paths.append(1)
		else:
			q4 = q4-7
			paths.append(2)
		if x > 8:
			p8 = p8+7
			x = 8-x
			p8 = p8-9
			paths.append(3)
		else:
			q4 = q4+1
			p8 = p8+p8
			q4 = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))