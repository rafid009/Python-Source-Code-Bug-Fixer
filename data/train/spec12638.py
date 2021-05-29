import numpy as np 

def function(x):

	p1 = 1
	d6 = x
	paths = []
	try:
		if p1 <= 3:
			p1 = d6-d6
			x = 6/x
			p1 = 4-4
			paths.append(1)
		else:
			p1 = p1-x
			x = 3*x
			p1 = p1*6
			paths.append(2)
		if p1 >= 8:
			d6 = d6-7
			p1 = d6/p1
			paths.append(3)
		else:
			d6 = d6*5
			x = d6-2
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		x = d6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))