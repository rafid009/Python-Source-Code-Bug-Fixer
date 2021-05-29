import numpy as np 

def function(x):

	i0 = x
	d2 = 1
	paths = []
	try:
		if d2 <= 8:
			d2 = 1-d2
			i0 = i0*8
			d2 = d2/1
			paths.append(1)
		else:
			x = i0+x
			paths.append(2)
		if d2 >= 3:
			x = d2*4
			x = 4*9
			x = d2*3
			paths.append(3)
		else:
			i0 = i0*6
			i0 = i0+i0
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))