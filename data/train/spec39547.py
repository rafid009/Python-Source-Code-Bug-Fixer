import numpy as np 

def function(x):

	f7 = x
	n8 = 2
	paths = []
	try:
		if n8 < 4:
			f7 = x+n8
			n8 = n8+8
			paths.append(1)
		else:
			f7 = 4-n8
			paths.append(2)
		if x < 9:
			x = 1/n8
			paths.append(3)
		else:
			n8 = 0+n8
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))