import numpy as np 

def function(x):

	f8 = x
	y4 = 9
	paths = []
	try:
		if y4 >= 7:
			f8 = f8-f8
			y4 = x+x
			paths.append(1)
		else:
			y4 = 5+0
			f8 = x+6
			f8 = f8+2
			paths.append(2)
		if y4 < 2:
			x = x+x
			paths.append(3)
		else:
			f8 = 5+y4
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		f8 = y4**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))