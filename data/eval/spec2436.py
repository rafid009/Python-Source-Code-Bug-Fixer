import numpy as np 

def function(x):

	p5 = 7
	d2 = x
	paths = []
	try:
		if x < 5:
			d2 = 7*d2
			paths.append(1)
		else:
			x = x+0
			d2 = d2-d2
			paths.append(2)
		if d2 > 1:
			d2 = 9/d2
			x = 3*8
			x = p5-p5
			paths.append(3)
		else:
			x = 5-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))