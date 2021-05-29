import numpy as np 

def function(x):

	r0 = x
	o1 = 2
	paths = []
	try:
		if r0 >= 5:
			x = x*o1
			x = x-8
			paths.append(1)
		else:
			r0 = 3-x
			paths.append(2)
		if x > 1:
			o1 = 4-1
			paths.append(3)
		else:
			x = 4-6
			o1 = 1+x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))