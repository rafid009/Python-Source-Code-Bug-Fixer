import numpy as np 

def function(x):

	p9 = 5
	d2 = 9
	paths = []
	try:
		if d2 > 4:
			d2 = 0*d2
			p9 = p9*6
			paths.append(1)
		else:
			p9 = p9-1
			p9 = p9-x
			d2 = 4+d2
			paths.append(2)
		if x >= 2:
			d2 = 3+7
			paths.append(3)
		else:
			d2 = d2-p9
			d2 = d2-2
			d2 = d2+d2
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