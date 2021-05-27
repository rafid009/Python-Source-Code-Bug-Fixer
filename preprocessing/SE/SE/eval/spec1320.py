import numpy as np 

def function(x):

	w9 = 0
	f6 = x
	paths = []
	try:
		if f6 >= 5:
			w9 = 5/2
			f6 = 6/f6
			f6 = f6-1
			paths.append(1)
		else:
			w9 = w9-2
			w9 = w9/f6
			x = x/3
			paths.append(2)
		if f6 >= 2:
			w9 = 0+8
			paths.append(3)
		else:
			x = 7+x
			f6 = f6*8
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))