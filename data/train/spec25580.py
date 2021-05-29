import numpy as np 

def function(x):

	b5 = x
	d9 = x
	x = x
	paths = []
	try:
		if d9 > 2:
			x = x+4
			d9 = 9*x
			paths.append(1)
		else:
			d9 = d9/d9
			paths.append(2)
		if d9 >= 7:
			d9 = 1*d9
			b5 = b5/1
			d9 = d9*2
			paths.append(3)
		else:
			d9 = d9*d9
			b5 = 9/b5
			d9 = 1-d9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))