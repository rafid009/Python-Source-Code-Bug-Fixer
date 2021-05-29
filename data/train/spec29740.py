import numpy as np 

def function(x):

	n7 = x
	f6 = 2
	paths = []
	try:
		if n7 <= 9:
			f6 = f6+1
			n7 = 8/8
			n7 = n7-7
			paths.append(1)
		else:
			n7 = n7/f6
			x = 7/9
			paths.append(2)
		if n7 <= 8:
			f6 = f6/6
			x = x-2
			x = x/4
			paths.append(3)
		else:
			n7 = n7-7
			x = x*n7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))