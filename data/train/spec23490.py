import numpy as np 

def function(x):

	p8 = 7
	d0 = 9
	paths = []
	try:
		if p8 > 4:
			p8 = 2-3
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if x > 9:
			x = x+6
			d0 = 4-d0
			d0 = p8+d0
			paths.append(3)
		else:
			x = d0/x
			x = 1-p8
			p8 = 7-p8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))