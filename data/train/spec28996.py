import numpy as np 

def function(x):

	o2 = x
	p7 = 2
	x = 5
	paths = []
	try:
		if o2 <= 7:
			o2 = o2/o2
			paths.append(1)
		else:
			o2 = x-o2
			o2 = o2-p7
			x = x+o2
			paths.append(2)
		if o2 >= 2:
			p7 = p7+2
			x = o2/x
			x = x+8
			paths.append(3)
		else:
			p7 = x+8
			o2 = o2*x
			p7 = p7*p7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))