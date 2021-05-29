import numpy as np 

def function(x):

	p2 = x
	o2 = x
	paths = []
	try:
		if o2 > 0:
			p2 = 4+p2
			paths.append(1)
		else:
			o2 = o2+p2
			o2 = o2-p2
			paths.append(2)
		if o2 <= 4:
			p2 = 1+p2
			o2 = o2+0
			paths.append(3)
		else:
			o2 = p2*o2
			x = 2-3
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))