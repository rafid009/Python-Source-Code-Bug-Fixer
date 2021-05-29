import numpy as np 

def function(x):

	i0 = x
	d1 = 7
	paths = []
	try:
		if x < 5:
			d1 = d1*4
			i0 = 7/i0
			x = 4/x
			paths.append(1)
		else:
			d1 = x-7
			x = x+2
			i0 = x/9
			paths.append(2)
		if d1 >= 6:
			d1 = 6+0
			paths.append(3)
		else:
			x = 5+i0
			d1 = d1+3
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		d1 = i0**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))