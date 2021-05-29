import numpy as np 

def function(x):

	d8 = x
	b7 = 9
	paths = []
	try:
		if d8 <= 6:
			b7 = 0-5
			x = 8/x
			b7 = 0/5
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if x >= 6:
			b7 = b7*1
			d8 = d8*b7
			paths.append(3)
		else:
			d8 = d8-0
			x = x/7
			x = b7+0
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		b7 = d8**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))