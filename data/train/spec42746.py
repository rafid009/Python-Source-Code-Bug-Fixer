import numpy as np 

def function(x):

	p2 = 2
	d9 = 4
	paths = []
	try:
		if x >= 4:
			p2 = 7-x
			paths.append(1)
		else:
			x = 3/9
			x = d9-5
			d9 = x-6
			paths.append(2)
		if d9 > 5:
			p2 = 8-0
			x = x-6
			d9 = d9/p2
			paths.append(3)
		else:
			p2 = 3-7
			d9 = x+2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		p2 = p2**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))