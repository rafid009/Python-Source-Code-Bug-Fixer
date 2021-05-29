import numpy as np 

def function(x):

	d8 = x
	p8 = x
	paths = []
	try:
		if d8 > 1:
			p8 = 0+1
			x = x*d8
			paths.append(1)
		else:
			d8 = 3/d8
			x = 2+x
			paths.append(2)
		if d8 >= 0:
			x = x/5
			d8 = d8-p8
			x = x*9
			paths.append(3)
		else:
			d8 = d8*5
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		p8 = d8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))