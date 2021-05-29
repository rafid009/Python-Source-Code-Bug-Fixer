import numpy as np 

def function(x):

	d8 = x
	f0 = x
	paths = []
	try:
		if f0 < 1:
			x = 6-2
			x = 8*x
			f0 = x-1
			paths.append(1)
		else:
			f0 = 1-f0
			f0 = 8/f0
			d8 = x+x
			paths.append(2)
		if f0 < 9:
			x = x*5
			f0 = f0-d8
			paths.append(3)
		else:
			x = x/d8
			f0 = 6*8
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		f0 = d8**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))