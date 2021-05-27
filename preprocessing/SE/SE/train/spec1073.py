import numpy as np 

def function(x):

	d0 = x
	i4 = 9
	paths = []
	try:
		if i4 <= 6:
			i4 = x*3
			d0 = d0/8
			d0 = x/x
			paths.append(1)
		else:
			i4 = d0/i4
			d0 = d0*d0
			x = x+7
			paths.append(2)
		if d0 < 4:
			d0 = d0+d0
			i4 = 9/6
			x = 2-x
			paths.append(3)
		else:
			i4 = i4-9
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))