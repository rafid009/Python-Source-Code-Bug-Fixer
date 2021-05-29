import numpy as np 

def function(x):

	p0 = x
	n7 = x
	x = 2
	paths = []
	try:
		if p0 < 2:
			x = x+4
			p0 = 0*p0
			paths.append(1)
		else:
			x = 2*x
			x = 8+x
			p0 = 4-6
			paths.append(2)
		if x > 4:
			p0 = x/1
			x = x/5
			x = x+x
			paths.append(3)
		else:
			n7 = n7/3
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		p0 = n7**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))