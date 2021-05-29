import numpy as np 

def function(x):

	f0 = 4
	o2 = 2
	paths = []
	try:
		if o2 >= 0:
			f0 = x/5
			paths.append(1)
		else:
			f0 = o2+2
			x = x-5
			f0 = 4*f0
			paths.append(2)
		if f0 < 3:
			o2 = o2-9
			o2 = 9-o2
			o2 = f0-4
			paths.append(3)
		else:
			f0 = f0/f0
			o2 = o2+f0
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))