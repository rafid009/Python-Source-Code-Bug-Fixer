import numpy as np 

def function(x):

	l1 = 0
	p4 = x
	x = 0
	paths = []
	try:
		if p4 >= 7:
			p4 = x-3
			l1 = l1*x
			l1 = x+3
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if p4 > 3:
			x = 1*x
			p4 = p4-x
			paths.append(3)
		else:
			p4 = 2*p4
			p4 = 1/9
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		l1 = p4**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))