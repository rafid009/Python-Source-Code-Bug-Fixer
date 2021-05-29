import numpy as np 

def function(x):

	o2 = x
	p4 = x
	paths = []
	try:
		if x < 0:
			x = x*3
			paths.append(1)
		else:
			o2 = 5-9
			paths.append(2)
		if o2 <= 0:
			o2 = p4-6
			p4 = 3+o2
			paths.append(3)
		else:
			p4 = p4*x
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		o2 = o2**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))