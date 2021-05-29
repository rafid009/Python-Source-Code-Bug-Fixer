import numpy as np 

def function(x):

	o9 = x
	f8 = 6
	paths = []
	try:
		if x < 4:
			f8 = o9/f8
			x = 5-9
			f8 = 7/f8
			paths.append(1)
		else:
			x = 1/x
			o9 = o9+4
			paths.append(2)
		if x <= 3:
			o9 = o9*2
			paths.append(3)
		else:
			f8 = f8+8
			f8 = 6*4
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))