import numpy as np 

def function(x):

	d4 = x
	i9 = 2
	paths = []
	try:
		if i9 < 7:
			x = x/6
			paths.append(1)
		else:
			d4 = d4*4
			x = x-1
			paths.append(2)
		if x < 5:
			d4 = d4+4
			d4 = 2-5
			paths.append(3)
		else:
			d4 = 6+8
			i9 = x*2
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		i9 = d4**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))