import numpy as np 

def function(x):

	o2 = x
	p4 = 8
	paths = []
	try:
		if p4 < 2:
			p4 = p4-6
			x = 2-x
			x = o2*x
			paths.append(1)
		else:
			p4 = o2+8
			paths.append(2)
		if o2 <= 4:
			x = 7+x
			paths.append(3)
		else:
			x = x*o2
			x = x-x
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		p4 = o2**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))