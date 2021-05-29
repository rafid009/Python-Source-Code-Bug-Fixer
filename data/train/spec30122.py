import numpy as np 

def function(x):

	d0 = x
	p6 = x
	paths = []
	try:
		if x < 9:
			p6 = p6-0
			x = x*8
			d0 = p6-5
			paths.append(1)
		else:
			x = 0+3
			p6 = 6-p6
			paths.append(2)
		if x <= 5:
			x = x/5
			d0 = x*d0
			paths.append(3)
		else:
			d0 = 6-d0
			d0 = d0/6
			x = x/5
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))