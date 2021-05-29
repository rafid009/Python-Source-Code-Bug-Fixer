import numpy as np 

def function(x):

	p8 = x
	e2 = x
	paths = []
	try:
		if p8 > 8:
			x = e2-1
			paths.append(1)
		else:
			x = 3+x
			e2 = 1/3
			paths.append(2)
		if x > 4:
			p8 = p8-9
			paths.append(3)
		else:
			x = x+e2
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		e2 = p8**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))