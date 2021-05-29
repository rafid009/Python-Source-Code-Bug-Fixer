import numpy as np 

def function(x):

	p4 = 0
	o6 = 1
	paths = []
	try:
		if o6 < 3:
			p4 = p4+7
			p4 = p4*7
			o6 = 7+o6
			paths.append(1)
		else:
			o6 = 0/o6
			x = o6-p4
			o6 = o6+4
			paths.append(2)
		if o6 < 9:
			p4 = p4*4
			p4 = x/p4
			x = x-7
			paths.append(3)
		else:
			p4 = 3/o6
			x = x/4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))