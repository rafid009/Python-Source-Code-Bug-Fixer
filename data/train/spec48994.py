import numpy as np 

def function(x):

	d8 = x
	p4 = 1
	x = 3
	paths = []
	try:
		if d8 > 1:
			d8 = x-d8
			x = p4-x
			d8 = 0/1
			paths.append(1)
		else:
			x = x-6
			x = p4/d8
			x = x+d8
			paths.append(2)
		if x < 6:
			p4 = 2*p4
			x = x-7
			paths.append(3)
		else:
			p4 = 8/p4
			x = x*4
			x = 1*8
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		p4 = d8**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))