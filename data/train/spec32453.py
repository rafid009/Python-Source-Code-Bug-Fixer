import numpy as np 

def function(x):

	p0 = 1
	l1 = x
	paths = []
	try:
		if l1 < 8:
			p0 = x/1
			l1 = l1+l1
			paths.append(1)
		else:
			l1 = l1/l1
			paths.append(2)
		if l1 >= 3:
			x = l1+4
			paths.append(3)
		else:
			l1 = 2-l1
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		p0 = p0**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))