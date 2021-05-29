import numpy as np 

def function(x):

	n8 = 2
	p0 = x
	paths = []
	try:
		if p0 <= 6:
			p0 = x-1
			n8 = x-0
			p0 = x/p0
			paths.append(1)
		else:
			p0 = p0*p0
			x = x+3
			paths.append(2)
		if n8 >= 2:
			p0 = 5+0
			paths.append(3)
		else:
			p0 = x/1
			x = p0+3
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		n8 = p0**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))