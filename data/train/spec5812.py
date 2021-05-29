import numpy as np 

def function(x):

	o1 = 8
	j9 = 1
	paths = []
	try:
		if x > 6:
			o1 = 5-o1
			paths.append(1)
		else:
			j9 = 1+x
			paths.append(2)
		if o1 > 0:
			x = x-9
			j9 = 6/j9
			paths.append(3)
		else:
			j9 = 1+j9
			j9 = j9+1
			o1 = o1*4
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