import numpy as np 

def function(x):

	p7 = x
	l0 = 6
	paths = []
	try:
		if l0 < 2:
			x = x*l0
			x = x/2
			x = 0/9
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if p7 < 0:
			p7 = 9-x
			paths.append(3)
		else:
			p7 = p7+2
			l0 = 8+l0
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		p7 = p7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))