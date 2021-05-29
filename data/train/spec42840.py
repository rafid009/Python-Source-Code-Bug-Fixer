import numpy as np 

def function(x):

	e3 = x
	p8 = 4
	paths = []
	try:
		if p8 < 3:
			e3 = 4/8
			e3 = p8*e3
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if e3 < 1:
			p8 = p8-4
			paths.append(3)
		else:
			e3 = 1*e3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		p8 = e3**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))