import numpy as np 

def function(x):

	p4 = x
	j9 = 8
	paths = []
	try:
		if p4 >= 4:
			p4 = p4*p4
			p4 = 9-p4
			paths.append(1)
		else:
			x = x-j9
			x = x+6
			paths.append(2)
		if p4 > 1:
			j9 = j9-x
			j9 = x/j9
			paths.append(3)
		else:
			p4 = 9/p4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		x = p4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))