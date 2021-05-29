import numpy as np 

def function(x):

	p0 = x
	g6 = 9
	paths = []
	try:
		if p0 >= 3:
			p0 = p0/p0
			x = x*1
			paths.append(1)
		else:
			x = 7+p0
			g6 = g6-8
			paths.append(2)
		if p0 >= 4:
			x = g6-x
			paths.append(3)
		else:
			p0 = x/9
			p0 = 2-p0
			g6 = g6+4
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