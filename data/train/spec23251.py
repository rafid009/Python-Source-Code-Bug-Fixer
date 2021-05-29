import numpy as np 

def function(x):

	p2 = 5
	d9 = x
	x = x
	paths = []
	try:
		if p2 > 3:
			x = x+5
			x = x+x
			x = x/4
			paths.append(1)
		else:
			d9 = d9/x
			x = 7/x
			paths.append(2)
		if p2 >= 4:
			x = d9-x
			d9 = 0/d9
			paths.append(3)
		else:
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))