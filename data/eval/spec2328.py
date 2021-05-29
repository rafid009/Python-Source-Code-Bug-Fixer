import numpy as np 

def function(x):

	n7 = 5
	p4 = x
	paths = []
	try:
		if n7 > 7:
			x = x+3
			n7 = n7+n7
			p4 = 4/p4
			paths.append(1)
		else:
			x = x+n7
			n7 = p4/x
			x = x/7
			paths.append(2)
		if x < 9:
			x = 7+n7
			paths.append(3)
		else:
			n7 = n7*x
			p4 = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))