import numpy as np 

def function(x):

	b7 = 4
	d9 = 3
	paths = []
	try:
		if b7 > 0:
			d9 = d9-b7
			paths.append(1)
		else:
			d9 = b7-3
			x = d9*x
			x = x-d9
			paths.append(2)
		if d9 < 7:
			b7 = d9-8
			d9 = d9+0
			b7 = b7*1
			paths.append(3)
		else:
			b7 = x+3
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		b7 = d9**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))