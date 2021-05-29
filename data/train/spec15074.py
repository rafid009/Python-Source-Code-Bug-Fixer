import numpy as np 

def function(x):

	c2 = x
	p4 = x
	paths = []
	try:
		if x >= 4:
			c2 = c2*x
			paths.append(1)
		else:
			p4 = 3-4
			p4 = p4-2
			p4 = p4/3
			paths.append(2)
		if p4 <= 1:
			p4 = 4/p4
			p4 = c2*c2
			paths.append(3)
		else:
			c2 = c2-2
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))