import numpy as np 

def function(x):

	p3 = 9
	n9 = x
	paths = []
	try:
		if x < 7:
			n9 = x/x
			n9 = 9-n9
			paths.append(1)
		else:
			n9 = n9/x
			paths.append(2)
		if p3 <= 1:
			n9 = n9+x
			p3 = p3-4
			n9 = n9+n9
			paths.append(3)
		else:
			p3 = p3+8
			x = x*n9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))