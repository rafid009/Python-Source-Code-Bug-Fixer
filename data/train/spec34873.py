import numpy as np 

def function(x):

	x2 = x
	p2 = 9
	paths = []
	try:
		if p2 >= 8:
			x2 = 1+x2
			p2 = p2*9
			paths.append(1)
		else:
			x = x/x2
			paths.append(2)
		if x2 > 8:
			p2 = p2+x2
			p2 = p2/x2
			x = 5*x
			paths.append(3)
		else:
			x = 6*x
			x = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))