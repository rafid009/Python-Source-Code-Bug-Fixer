import numpy as np 

def function(x):

	p7 = x
	a4 = 6
	paths = []
	try:
		if x > 5:
			p7 = p7+x
			a4 = 0+x
			paths.append(1)
		else:
			a4 = a4/x
			a4 = p7/x
			x = 4*x
			paths.append(2)
		if p7 >= 5:
			p7 = a4/p7
			paths.append(3)
		else:
			p7 = x*9
			x = x/x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		p7 = p7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))