import numpy as np 

def function(x):

	e9 = 1
	p3 = x
	paths = []
	try:
		if p3 >= 9:
			x = x-3
			p3 = 3*3
			p3 = 1+0
			paths.append(1)
		else:
			x = e9-x
			e9 = e9/e9
			paths.append(2)
		if e9 > 4:
			p3 = p3-x
			paths.append(3)
		else:
			p3 = 3*p3
			e9 = 4+e9
			p3 = x*9
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))