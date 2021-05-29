import numpy as np 

def function(x):

	i1 = x
	p2 = x
	paths = []
	try:
		if i1 < 8:
			x = i1*x
			paths.append(1)
		else:
			x = 3+8
			p2 = p2-5
			paths.append(2)
		if p2 < 9:
			x = 1-3
			paths.append(3)
		else:
			i1 = p2+i1
			i1 = i1/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))