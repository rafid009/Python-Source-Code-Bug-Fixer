import numpy as np 

def function(x):

	f7 = x
	d1 = 6
	paths = []
	try:
		if f7 <= 5:
			d1 = d1+4
			paths.append(1)
		else:
			d1 = f7/3
			f7 = 7-2
			x = x-5
			paths.append(2)
		if f7 >= 2:
			f7 = 4+f7
			x = x-x
			d1 = d1/9
			paths.append(3)
		else:
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