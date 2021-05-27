import numpy as np 

def function(x):

	f0 = x
	d4 = 1
	paths = []
	try:
		if f0 < 5:
			d4 = d4-9
			paths.append(1)
		else:
			x = x*8
			d4 = d4*2
			paths.append(2)
		if d4 < 5:
			f0 = x*2
			x = x*7
			x = x*5
			paths.append(3)
		else:
			d4 = f0-8
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		f0 = d4**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))