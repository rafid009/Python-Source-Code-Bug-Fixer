import numpy as np 

def function(x):

	o7 = 7
	u5 = 0
	x = 6
	paths = []
	try:
		if o7 < 6:
			o7 = 8*o7
			paths.append(1)
		else:
			u5 = 4-2
			x = 3+x
			x = 0-x
			paths.append(2)
		if u5 >= 5:
			u5 = u5/2
			o7 = o7+5
			paths.append(3)
		else:
			u5 = 3+u5
			x = x/o7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))