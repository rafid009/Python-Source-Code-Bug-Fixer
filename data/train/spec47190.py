import numpy as np 

def function(x):

	n9 = x
	f7 = x
	paths = []
	try:
		if x < 0:
			x = 5-5
			x = x-1
			x = f7-n9
			paths.append(1)
		else:
			n9 = 4/4
			x = x/1
			n9 = 3*n9
			paths.append(2)
		if f7 > 6:
			n9 = n9*6
			f7 = 2*f7
			n9 = n9/2
			paths.append(3)
		else:
			f7 = 8/f7
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		n9 = f7**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))