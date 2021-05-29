import numpy as np 

def function(x):

	r4 = 9
	o2 = 5
	paths = []
	try:
		if r4 >= 2:
			x = 2+x
			o2 = 4-r4
			r4 = 9/4
			paths.append(1)
		else:
			x = x/3
			o2 = o2/o2
			paths.append(2)
		if o2 < 5:
			x = x-o2
			paths.append(3)
		else:
			o2 = o2-r4
			x = 0+x
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