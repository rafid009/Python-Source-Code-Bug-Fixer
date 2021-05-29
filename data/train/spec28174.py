import numpy as np 

def function(x):

	p4 = 6
	o6 = 0
	paths = []
	try:
		if o6 < 8:
			x = x+2
			o6 = o6-p4
			paths.append(1)
		else:
			o6 = 2*o6
			paths.append(2)
		if p4 <= 8:
			p4 = p4/8
			p4 = p4+8
			paths.append(3)
		else:
			o6 = 4/o6
			o6 = o6+4
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o6 = x**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))