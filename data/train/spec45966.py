import numpy as np 

def function(x):

	p5 = 5
	d0 = x
	paths = []
	try:
		if d0 < 9:
			d0 = d0+6
			p5 = 2+p5
			paths.append(1)
		else:
			p5 = 5*p5
			paths.append(2)
		if x <= 8:
			p5 = p5+5
			d0 = d0/5
			d0 = 8+4
			paths.append(3)
		else:
			x = 4-3
			x = 2*p5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))