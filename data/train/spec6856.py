import numpy as np 

def function(x):

	i1 = x
	p1 = 5
	paths = []
	try:
		if i1 < 9:
			x = 5+x
			x = 0+x
			x = 1*3
			paths.append(1)
		else:
			x = p1-x
			paths.append(2)
		if i1 >= 5:
			x = 6+x
			paths.append(3)
		else:
			p1 = p1+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))