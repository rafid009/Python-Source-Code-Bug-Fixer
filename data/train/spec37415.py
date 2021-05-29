import numpy as np 

def function(x):

	p4 = 9
	d6 = 6
	x = x
	paths = []
	try:
		if p4 > 6:
			d6 = d6+7
			paths.append(1)
		else:
			d6 = x/5
			p4 = p4*d6
			paths.append(2)
		if x <= 2:
			p4 = d6-7
			x = 1*x
			paths.append(3)
		else:
			d6 = d6/3
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))