import numpy as np 

def function(x):

	d2 = 4
	v2 = x
	paths = []
	try:
		if d2 > 1:
			x = 4*8
			v2 = 7/v2
			d2 = 3-5
			paths.append(1)
		else:
			d2 = d2-v2
			paths.append(2)
		if d2 < 2:
			d2 = x/d2
			d2 = 1+5
			paths.append(3)
		else:
			v2 = v2/x
			d2 = x+d2
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		x = v2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))