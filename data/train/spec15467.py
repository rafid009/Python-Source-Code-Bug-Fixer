import numpy as np 

def function(x):

	e9 = x
	p2 = x
	paths = []
	try:
		if x < 9:
			e9 = e9/1
			e9 = e9-7
			p2 = p2*9
			paths.append(1)
		else:
			p2 = p2-1
			paths.append(2)
		if x <= 4:
			e9 = e9-p2
			p2 = p2/4
			paths.append(3)
		else:
			x = x*6
			x = x/x
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))