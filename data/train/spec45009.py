import numpy as np 

def function(x):

	d4 = x
	b9 = x
	paths = []
	try:
		if d4 <= 7:
			x = x-7
			b9 = 2+1
			paths.append(1)
		else:
			b9 = b9+7
			d4 = 8-4
			paths.append(2)
		if x >= 5:
			b9 = b9-0
			b9 = d4-2
			paths.append(3)
		else:
			b9 = x/x
			x = b9+x
			x = x/6
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		b9 = d4**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))