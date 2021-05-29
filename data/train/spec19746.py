import numpy as np 

def function(x):

	e1 = 7
	p8 = x
	paths = []
	try:
		if x < 2:
			p8 = 9*p8
			e1 = p8/p8
			x = 7/9
			paths.append(1)
		else:
			p8 = p8+9
			paths.append(2)
		if p8 < 1:
			x = e1+6
			paths.append(3)
		else:
			p8 = 1/2
			e1 = x+e1
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))