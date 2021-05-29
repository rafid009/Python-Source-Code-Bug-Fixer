import numpy as np 

def function(x):

	n5 = x
	f6 = x
	paths = []
	try:
		if f6 > 4:
			n5 = 8/8
			x = 0-f6
			n5 = n5+x
			paths.append(1)
		else:
			n5 = f6/3
			n5 = n5*3
			paths.append(2)
		if n5 > 1:
			x = x+5
			paths.append(3)
		else:
			x = x+5
			f6 = n5*7
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))