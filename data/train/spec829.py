import numpy as np 

def function(x):

	b8 = x
	d5 = 5
	paths = []
	try:
		if x <= 3:
			b8 = 7+1
			b8 = b8+d5
			b8 = 4+b8
			paths.append(1)
		else:
			x = 5-2
			x = 0*x
			b8 = x/b8
			paths.append(2)
		if d5 > 3:
			d5 = d5/5
			d5 = d5-3
			d5 = 5-3
			paths.append(3)
		else:
			b8 = 4-9
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