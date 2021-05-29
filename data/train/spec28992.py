import numpy as np 

def function(x):

	p6 = 2
	o2 = x
	paths = []
	try:
		if o2 <= 3:
			o2 = o2*8
			paths.append(1)
		else:
			p6 = p6-2
			p6 = p6-o2
			o2 = 0+p6
			paths.append(2)
		if p6 > 2:
			o2 = 0/o2
			x = 2-x
			paths.append(3)
		else:
			x = x+6
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		o2 = p6**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))