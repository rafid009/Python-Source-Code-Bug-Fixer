import numpy as np 

def function(x):

	o4 = 2
	j7 = 7
	paths = []
	try:
		if o4 > 8:
			j7 = 0-j7
			x = x-9
			j7 = j7*j7
			paths.append(1)
		else:
			x = x*6
			o4 = j7/1
			x = 4/x
			paths.append(2)
		if o4 >= 7:
			o4 = 2-o4
			x = x+o4
			x = x-7
			paths.append(3)
		else:
			x = x-1
			j7 = 8+j7
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))