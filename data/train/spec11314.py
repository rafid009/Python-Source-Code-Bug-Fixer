import numpy as np 

def function(x):

	f6 = 9
	o7 = x
	paths = []
	try:
		if f6 > 5:
			o7 = 6*o7
			o7 = x+f6
			f6 = 2/f6
			paths.append(1)
		else:
			x = 3/x
			x = x-0
			paths.append(2)
		if o7 > 1:
			x = 5-x
			o7 = 3/o7
			paths.append(3)
		else:
			x = x+x
			o7 = 0-f6
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		f6 = o7**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))