import numpy as np 

def function(x):

	f7 = x
	d0 = x
	paths = []
	try:
		if d0 < 2:
			x = x*8
			f7 = f7/1
			x = 2*8
			paths.append(1)
		else:
			d0 = 4*d0
			f7 = d0/9
			paths.append(2)
		if d0 > 4:
			f7 = 8-f7
			x = x/9
			paths.append(3)
		else:
			f7 = 1+1
			f7 = 7*8
			d0 = d0+2
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))