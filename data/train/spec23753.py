import numpy as np 

def function(x):

	d4 = x
	b8 = 3
	paths = []
	try:
		if d4 < 3:
			d4 = d4*2
			d4 = d4+4
			paths.append(1)
		else:
			x = d4-2
			x = d4*x
			x = d4+2
			paths.append(2)
		if b8 >= 3:
			b8 = x/b8
			x = 5-1
			paths.append(3)
		else:
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		b8 = d4**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))