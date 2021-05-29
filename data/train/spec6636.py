import numpy as np 

def function(x):

	p2 = 2
	n1 = x
	paths = []
	try:
		if p2 < 3:
			n1 = 1+n1
			p2 = n1-p2
			n1 = n1+x
			paths.append(1)
		else:
			p2 = 1+p2
			n1 = 2+4
			n1 = n1+n1
			paths.append(2)
		if p2 >= 7:
			x = 6*5
			x = 8/x
			paths.append(3)
		else:
			p2 = 6+p2
			n1 = n1+p2
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))