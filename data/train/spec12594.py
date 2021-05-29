import numpy as np 

def function(x):

	f0 = 4
	o7 = x
	x = x
	paths = []
	try:
		if o7 >= 9:
			o7 = 2/o7
			f0 = 8/f0
			f0 = 1-f0
			paths.append(1)
		else:
			o7 = 6-f0
			x = x-o7
			paths.append(2)
		if o7 > 0:
			o7 = 0+o7
			f0 = o7/9
			paths.append(3)
		else:
			f0 = f0*3
			o7 = o7*0
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))