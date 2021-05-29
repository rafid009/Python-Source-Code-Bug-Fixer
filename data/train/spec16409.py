import numpy as np 

def function(x):

	p2 = x
	p0 = 9
	paths = []
	try:
		if p0 > 6:
			p0 = 0/p0
			p0 = p0+x
			x = 3/x
			paths.append(1)
		else:
			x = p2/2
			x = 1+4
			p2 = 5+0
			paths.append(2)
		if p2 <= 3:
			p2 = p2/5
			p2 = 3/p2
			x = 3+x
			paths.append(3)
		else:
			p2 = x/p0
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		p0 = p0**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))