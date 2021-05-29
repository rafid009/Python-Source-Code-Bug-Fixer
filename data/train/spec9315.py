import numpy as np 

def function(x):

	i0 = x
	d8 = x
	paths = []
	try:
		if x < 1:
			x = 6+x
			d8 = d8/1
			d8 = 1/d8
			paths.append(1)
		else:
			x = i0-i0
			paths.append(2)
		if d8 < 5:
			x = 0*x
			d8 = d8/9
			paths.append(3)
		else:
			i0 = 1*8
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		i0 = d8**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))