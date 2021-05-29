import numpy as np 

def function(x):

	d4 = 7
	i4 = 6
	paths = []
	try:
		if i4 < 4:
			d4 = x*1
			x = x*7
			x = d4-x
			paths.append(1)
		else:
			x = x+1
			i4 = i4+3
			d4 = d4*1
			paths.append(2)
		if i4 > 3:
			x = x+8
			d4 = 1+d4
			d4 = 9/d4
			paths.append(3)
		else:
			i4 = 0+9
			d4 = 9-d4
			x = i4+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))