import numpy as np 

def function(x):

	p4 = x
	l4 = x
	paths = []
	try:
		if x > 5:
			p4 = p4-l4
			x = x+4
			paths.append(1)
		else:
			p4 = 3-p4
			l4 = 7+l4
			paths.append(2)
		if p4 >= 3:
			p4 = 4/l4
			paths.append(3)
		else:
			p4 = p4+5
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		l4 = p4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))