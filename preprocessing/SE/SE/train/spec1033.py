import numpy as np 

def function(x):

	o7 = 8
	f0 = x
	paths = []
	try:
		if f0 >= 4:
			x = 5-x
			o7 = f0-o7
			paths.append(1)
		else:
			f0 = f0*8
			paths.append(2)
		if o7 <= 2:
			o7 = o7/o7
			x = 9-x
			paths.append(3)
		else:
			o7 = 2*o7
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))