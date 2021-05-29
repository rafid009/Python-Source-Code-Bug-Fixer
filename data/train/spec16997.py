import numpy as np 

def function(x):

	v1 = 6
	d8 = 3
	paths = []
	try:
		if v1 < 2:
			d8 = d8*1
			x = x-x
			paths.append(1)
		else:
			v1 = x-v1
			x = 6-x
			paths.append(2)
		if d8 <= 1:
			x = 9*8
			d8 = 1+d8
			paths.append(3)
		else:
			d8 = x+8
			v1 = v1+1
			x = x+5
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		d8 = d8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))