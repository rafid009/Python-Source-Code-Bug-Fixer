import numpy as np 

def function(x):

	p6 = x
	n2 = 4
	x = x
	paths = []
	try:
		if p6 >= 8:
			n2 = p6+3
			x = 1*x
			p6 = 3/p6
			paths.append(1)
		else:
			x = 1-0
			paths.append(2)
		if x > 0:
			x = x+x
			n2 = 4*n2
			x = x*4
			paths.append(3)
		else:
			n2 = 3/4
			p6 = 8/p6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p6 = p6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))