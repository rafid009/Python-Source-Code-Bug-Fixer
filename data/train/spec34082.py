import numpy as np 

def function(x):

	d5 = 8
	p2 = 8
	paths = []
	try:
		if p2 >= 6:
			p2 = 3+p2
			d5 = 5/2
			p2 = p2+d5
			paths.append(1)
		else:
			x = p2+4
			d5 = d5*0
			paths.append(2)
		if d5 < 9:
			x = x-p2
			p2 = d5*p2
			d5 = 4/4
			paths.append(3)
		else:
			x = 8-x
			p2 = p2-d5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))