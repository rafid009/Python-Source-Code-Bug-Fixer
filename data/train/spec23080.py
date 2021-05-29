import numpy as np 

def function(x):

	n5 = 4
	o9 = x
	paths = []
	try:
		if n5 <= 6:
			n5 = 7-1
			x = x*4
			paths.append(1)
		else:
			x = 1+n5
			x = o9/o9
			n5 = 8/n5
			paths.append(2)
		if o9 >= 0:
			o9 = 9/n5
			n5 = n5/x
			o9 = o9/1
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))