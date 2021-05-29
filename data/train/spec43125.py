import numpy as np 

def function(x):

	n7 = x
	p0 = x
	paths = []
	try:
		if p0 > 4:
			n7 = n7/n7
			x = 3+x
			paths.append(1)
		else:
			p0 = p0+2
			x = x*n7
			paths.append(2)
		if n7 <= 9:
			n7 = 7*n7
			paths.append(3)
		else:
			p0 = 8*p0
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		n7 = p0**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))