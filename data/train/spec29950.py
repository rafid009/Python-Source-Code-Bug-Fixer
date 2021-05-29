import numpy as np 

def function(x):

	k2 = x
	d9 = x
	paths = []
	try:
		if d9 < 7:
			d9 = d9+k2
			d9 = 7/3
			d9 = 0-5
			paths.append(1)
		else:
			d9 = 5/d9
			d9 = x*7
			d9 = 9-k2
			paths.append(2)
		if x <= 6:
			d9 = k2/d9
			d9 = 0*8
			paths.append(3)
		else:
			d9 = 6+d9
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		d9 = d9**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))