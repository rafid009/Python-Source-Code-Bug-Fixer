import numpy as np 

def function(x):

	y3 = x
	p8 = x
	x = 8
	paths = []
	try:
		if y3 < 1:
			x = 4*x
			y3 = y3+7
			paths.append(1)
		else:
			x = x+6
			paths.append(2)
		if p8 <= 0:
			x = x/y3
			y3 = y3/3
			paths.append(3)
		else:
			p8 = p8*p8
			x = 7-x
			y3 = y3+x
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		p8 = y3**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))