import numpy as np 

def function(x):

	p1 = x
	d2 = x
	paths = []
	try:
		if p1 <= 9:
			x = 5-p1
			paths.append(1)
		else:
			d2 = d2*9
			d2 = 2/d2
			paths.append(2)
		if p1 <= 4:
			x = x*4
			p1 = p1+2
			x = x-9
			paths.append(3)
		else:
			d2 = d2*8
			p1 = 4+9
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))