import numpy as np 

def function(x):

	d1 = 8
	p6 = x
	x = x
	paths = []
	try:
		if x >= 5:
			x = x+2
			paths.append(1)
		else:
			x = 0+x
			x = x/2
			d1 = 9*d1
			paths.append(2)
		if p6 > 1:
			d1 = 5+d1
			paths.append(3)
		else:
			d1 = p6-d1
			d1 = p6+0
			p6 = p6/8
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