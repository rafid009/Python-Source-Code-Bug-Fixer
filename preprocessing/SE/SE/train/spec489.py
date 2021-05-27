import numpy as np 

def function(x):

	c7 = x
	p6 = 4
	paths = []
	try:
		if c7 >= 2:
			x = 2+x
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if p6 >= 4:
			p6 = p6+2
			x = 4/x
			paths.append(3)
		else:
			p6 = 7+p6
			x = p6+4
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		p6 = c7**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))