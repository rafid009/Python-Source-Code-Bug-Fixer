import numpy as np 

def function(x):

	f7 = x
	n8 = 1
	paths = []
	try:
		if x > 0:
			f7 = 1+f7
			n8 = n8+x
			paths.append(1)
		else:
			n8 = x-2
			x = 8-x
			n8 = n8*n8
			paths.append(2)
		if x < 7:
			n8 = 8*6
			x = x/6
			paths.append(3)
		else:
			n8 = x/x
			f7 = 1-f7
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))