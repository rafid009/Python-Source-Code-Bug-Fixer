import numpy as np 

def function(x):

	d1 = 0
	b2 = 6
	paths = []
	try:
		if d1 <= 8:
			b2 = b2+2
			paths.append(1)
		else:
			b2 = b2/d1
			x = 9*2
			d1 = b2-b2
			paths.append(2)
		if b2 >= 8:
			x = x+0
			paths.append(3)
		else:
			d1 = d1/6
			d1 = 8-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))