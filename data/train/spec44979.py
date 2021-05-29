import numpy as np 

def function(x):

	n3 = x
	p4 = 3
	x = 4
	paths = []
	try:
		if x > 3:
			p4 = 4-p4
			paths.append(1)
		else:
			p4 = 5/2
			paths.append(2)
		if n3 >= 5:
			x = 5+p4
			n3 = n3+6
			paths.append(3)
		else:
			n3 = 9/n3
			p4 = 4*p4
			n3 = n3/x
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))