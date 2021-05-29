import numpy as np 

def function(x):

	p1 = x
	n2 = x
	paths = []
	try:
		if n2 > 2:
			x = p1/4
			p1 = p1-2
			paths.append(1)
		else:
			p1 = 3*n2
			paths.append(2)
		if n2 <= 8:
			p1 = 4+p1
			n2 = x*6
			paths.append(3)
		else:
			x = 1+p1
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		x = p1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))