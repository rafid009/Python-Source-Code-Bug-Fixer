import numpy as np 

def function(x):

	c3 = x
	o0 = 9
	paths = []
	try:
		if o0 >= 4:
			x = x/3
			x = 2/o0
			paths.append(1)
		else:
			x = 6+1
			o0 = c3+o0
			paths.append(2)
		if o0 >= 7:
			c3 = c3+1
			paths.append(3)
		else:
			x = x-x
			c3 = o0/8
			x = o0-4
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		o0 = c3**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))