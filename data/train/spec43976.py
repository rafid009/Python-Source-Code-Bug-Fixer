import numpy as np 

def function(x):

	x6 = x
	o1 = x
	paths = []
	try:
		if o1 > 0:
			x6 = x+x6
			x = x6*6
			x = 0-x
			paths.append(1)
		else:
			x = x*3
			x6 = 5+x6
			x = 6*x
			paths.append(2)
		if x <= 2:
			x6 = x6*8
			o1 = 9+o1
			paths.append(3)
		else:
			x = x-2
			x = x/1
			x6 = x6+x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))