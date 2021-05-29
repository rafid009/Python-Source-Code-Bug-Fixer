import numpy as np 

def function(x):

	v2 = 3
	d0 = 4
	paths = []
	try:
		if v2 <= 6:
			v2 = 8*x
			x = x+3
			d0 = 3*d0
			paths.append(1)
		else:
			d0 = d0-4
			v2 = 2/v2
			paths.append(2)
		if v2 <= 1:
			x = 4*v2
			v2 = x-v2
			x = 3+9
			paths.append(3)
		else:
			v2 = v2+8
			v2 = v2/v2
			x = 4+x
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