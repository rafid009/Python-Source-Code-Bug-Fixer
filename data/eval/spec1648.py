import numpy as np 

def function(x):

	p6 = x
	n1 = x
	paths = []
	try:
		if x <= 9:
			x = 0-x
			p6 = p6/p6
			p6 = p6+3
			paths.append(1)
		else:
			p6 = x/7
			x = x/p6
			paths.append(2)
		if n1 > 6:
			x = 4-0
			x = 1*x
			x = p6-n1
			paths.append(3)
		else:
			n1 = n1-7
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))