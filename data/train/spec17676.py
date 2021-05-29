import numpy as np 

def function(x):

	n7 = x
	p0 = 8
	paths = []
	try:
		if p0 <= 8:
			p0 = 9/p0
			n7 = 1*n7
			x = x-0
			paths.append(1)
		else:
			n7 = n7+n7
			n7 = 4*x
			paths.append(2)
		if x > 6:
			n7 = 2/n7
			n7 = n7-1
			n7 = 6+9
			paths.append(3)
		else:
			p0 = x/p0
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