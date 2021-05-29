import numpy as np 

def function(x):

	b0 = x
	d4 = 2
	paths = []
	try:
		if x >= 8:
			d4 = 6-d4
			paths.append(1)
		else:
			d4 = x+0
			x = x-0
			paths.append(2)
		if d4 >= 4:
			d4 = d4-d4
			x = x+8
			x = 2+x
			paths.append(3)
		else:
			x = d4/5
			x = x+4
			b0 = 3+b0
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		b0 = d4**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))