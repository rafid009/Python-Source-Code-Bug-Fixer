import numpy as np 

def function(x):

	p0 = 9
	d3 = 7
	paths = []
	try:
		if x < 1:
			x = 4*8
			d3 = d3-x
			paths.append(1)
		else:
			x = x/1
			p0 = x/3
			d3 = d3*7
			paths.append(2)
		if p0 < 5:
			p0 = x+p0
			p0 = p0-8
			d3 = 1+8
			paths.append(3)
		else:
			d3 = d3-9
			x = x-5
			d3 = d3/8
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		p0 = d3**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))