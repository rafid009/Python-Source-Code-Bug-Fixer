import numpy as np 

def function(x):

	p4 = 5
	o2 = x
	x = 1
	paths = []
	try:
		if x < 2:
			x = x*3
			o2 = o2/o2
			paths.append(1)
		else:
			x = p4+4
			o2 = o2-7
			paths.append(2)
		if x < 3:
			x = 4/p4
			x = o2*2
			p4 = p4+6
			paths.append(3)
		else:
			p4 = p4-6
			x = x+8
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		x = p4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))