import numpy as np 

def function(x):

	p0 = x
	k7 = x
	x = x
	paths = []
	try:
		if k7 >= 6:
			x = x/7
			paths.append(1)
		else:
			p0 = p0*3
			p0 = 1/p0
			x = x+k7
			paths.append(2)
		if x <= 4:
			p0 = p0+p0
			paths.append(3)
		else:
			p0 = p0/6
			p0 = x+p0
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