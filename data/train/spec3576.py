import numpy as np 

def function(x):

	f9 = 1
	o2 = x
	paths = []
	try:
		if o2 > 3:
			o2 = 1*o2
			paths.append(1)
		else:
			f9 = f9*f9
			o2 = 2-o2
			paths.append(2)
		if f9 >= 7:
			o2 = o2*2
			o2 = 0-0
			paths.append(3)
		else:
			x = x*7
			o2 = o2*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))