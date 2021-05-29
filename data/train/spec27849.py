import numpy as np 

def function(x):

	d0 = x
	i6 = 5
	paths = []
	try:
		if d0 <= 8:
			d0 = i6/d0
			paths.append(1)
		else:
			i6 = i6+4
			paths.append(2)
		if d0 >= 1:
			i6 = 2-8
			x = x*8
			x = x+6
			paths.append(3)
		else:
			x = d0/5
			i6 = 1/i6
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		d0 = i6**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))