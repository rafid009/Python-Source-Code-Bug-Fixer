import numpy as np 

def function(x):

	p6 = 2
	d6 = 8
	paths = []
	try:
		if x > 4:
			x = d6/x
			p6 = p6+p6
			x = x-1
			paths.append(1)
		else:
			d6 = d6+6
			paths.append(2)
		if d6 < 3:
			d6 = 8*3
			x = x+d6
			x = d6+x
			paths.append(3)
		else:
			d6 = x+8
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		p6 = d6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))