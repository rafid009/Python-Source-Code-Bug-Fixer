import numpy as np 

def function(x):

	p9 = 1
	d6 = 9
	paths = []
	try:
		if d6 > 0:
			p9 = p9*p9
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if x > 9:
			d6 = d6+9
			d6 = 6/d6
			paths.append(3)
		else:
			x = x*4
			p9 = 6/p9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))