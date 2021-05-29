import numpy as np 

def function(x):

	y7 = x
	p8 = x
	x = 1
	paths = []
	try:
		if x >= 9:
			y7 = 4*y7
			x = x*9
			paths.append(1)
		else:
			y7 = 4+y7
			p8 = p8*6
			y7 = y7*p8
			paths.append(2)
		if p8 > 6:
			y7 = 6+y7
			p8 = p8*p8
			y7 = 8/y7
			paths.append(3)
		else:
			y7 = 5-y7
			x = p8*7
			x = x/p8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))