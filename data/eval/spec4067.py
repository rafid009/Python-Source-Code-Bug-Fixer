import numpy as np 

def function(x):

	p0 = x
	n9 = 2
	paths = []
	try:
		if p0 >= 4:
			x = x/7
			p0 = p0/7
			x = 3-x
			paths.append(1)
		else:
			n9 = 6*6
			x = n9*2
			p0 = 9+n9
			paths.append(2)
		if n9 <= 0:
			x = 0/x
			x = 1+x
			paths.append(3)
		else:
			p0 = p0+x
			p0 = p0/x
			x = x/3
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x = p0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))