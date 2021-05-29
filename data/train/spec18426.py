import numpy as np 

def function(x):

	d0 = 1
	p6 = 7
	paths = []
	try:
		if p6 > 4:
			p6 = 2-p6
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if p6 <= 4:
			d0 = 3*p6
			d0 = 7-p6
			paths.append(3)
		else:
			d0 = 9+5
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p6 = p6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))