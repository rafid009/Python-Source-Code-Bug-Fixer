import numpy as np 

def function(x):

	n5 = x
	f7 = x
	paths = []
	try:
		if f7 > 1:
			n5 = n5+6
			n5 = 6-n5
			paths.append(1)
		else:
			f7 = f7+3
			n5 = 8/n5
			x = 6/f7
			paths.append(2)
		if f7 >= 2:
			n5 = 7-0
			f7 = f7-f7
			f7 = 4+1
			paths.append(3)
		else:
			f7 = f7/6
			f7 = f7/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))