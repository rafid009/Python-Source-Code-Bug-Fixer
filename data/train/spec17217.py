import numpy as np 

def function(x):

	p6 = x
	p4 = 2
	paths = []
	try:
		if p6 > 9:
			x = p6*7
			x = 3+x
			p4 = p4/x
			paths.append(1)
		else:
			x = x/5
			x = x*2
			paths.append(2)
		if p6 > 5:
			x = 1*5
			x = x-8
			p4 = 0-p6
			paths.append(3)
		else:
			x = x+p4
			p6 = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))