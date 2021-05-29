import numpy as np 

def function(x):

	n6 = 4
	p7 = 7
	paths = []
	try:
		if n6 >= 3:
			p7 = n6+1
			n6 = 4+p7
			x = 8-x
			paths.append(1)
		else:
			p7 = p7*9
			p7 = p7/n6
			paths.append(2)
		if n6 >= 1:
			n6 = x-4
			p7 = 6/p7
			paths.append(3)
		else:
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		p7 = n6**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))