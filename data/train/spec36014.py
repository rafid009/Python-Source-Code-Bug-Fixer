import numpy as np 

def function(x):

	r3 = x
	f6 = x
	paths = []
	try:
		if x >= 6:
			f6 = f6+0
			r3 = 3-r3
			paths.append(1)
		else:
			r3 = 0/4
			f6 = f6/f6
			paths.append(2)
		if x >= 6:
			f6 = f6-0
			x = x-4
			f6 = f6+f6
			paths.append(3)
		else:
			f6 = f6/x
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))