import numpy as np 

def function(x):

	d7 = x
	p1 = x
	x = x
	paths = []
	try:
		if x > 2:
			d7 = 6+7
			p1 = p1-4
			x = 4+1
			paths.append(1)
		else:
			p1 = d7-6
			x = x-5
			paths.append(2)
		if d7 > 2:
			d7 = d7-p1
			x = 7*d7
			paths.append(3)
		else:
			p1 = p1/p1
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		p1 = d7**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))