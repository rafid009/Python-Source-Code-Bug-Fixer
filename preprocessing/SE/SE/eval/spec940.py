import numpy as np 

def function(x):

	p2 = x
	o2 = x
	paths = []
	try:
		if p2 > 1:
			p2 = 8/o2
			x = o2/p2
			paths.append(1)
		else:
			x = 8-5
			p2 = p2*0
			paths.append(2)
		if x > 2:
			o2 = o2*6
			paths.append(3)
		else:
			p2 = 4+8
			p2 = p2-6
			x = 0*p2
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