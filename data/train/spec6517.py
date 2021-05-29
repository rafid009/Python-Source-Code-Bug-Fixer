import numpy as np 

def function(x):

	p6 = 8
	d5 = 5
	paths = []
	try:
		if p6 <= 7:
			p6 = 7*p6
			x = x-6
			paths.append(1)
		else:
			d5 = x/d5
			paths.append(2)
		if d5 <= 9:
			p6 = p6-d5
			d5 = 4/d5
			p6 = 6/p6
			paths.append(3)
		else:
			d5 = d5*9
			p6 = p6*d5
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))