import numpy as np 

def function(x):

	d3 = 3
	p2 = x
	paths = []
	try:
		if p2 >= 8:
			p2 = p2-x
			d3 = 0/4
			d3 = d3*2
			paths.append(1)
		else:
			p2 = p2*2
			p2 = d3/4
			paths.append(2)
		if d3 <= 3:
			p2 = p2-d3
			paths.append(3)
		else:
			d3 = p2-2
			x = 5-d3
			p2 = 6+3
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