import numpy as np 

def function(x):

	d4 = 7
	b6 = 6
	paths = []
	try:
		if b6 <= 4:
			d4 = 3-d4
			b6 = b6*2
			x = x-4
			paths.append(1)
		else:
			d4 = d4/x
			b6 = x/b6
			b6 = 2-9
			paths.append(2)
		if b6 < 0:
			x = 1+x
			paths.append(3)
		else:
			b6 = b6-d4
			b6 = b6-3
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		b6 = d4**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))