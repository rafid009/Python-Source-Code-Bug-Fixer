import numpy as np 

def function(x):

	d1 = 6
	k2 = x
	paths = []
	try:
		if x > 9:
			x = x-k2
			x = d1+9
			x = 5+1
			paths.append(1)
		else:
			d1 = x+d1
			x = 0-x
			paths.append(2)
		if x > 7:
			x = 8*d1
			x = x-5
			k2 = k2-1
			paths.append(3)
		else:
			d1 = 9+d1
			k2 = d1*d1
			d1 = d1*1
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		d1 = k2**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))