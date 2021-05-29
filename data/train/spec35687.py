import numpy as np 

def function(x):

	k5 = x
	w0 = x
	paths = []
	try:
		if x < 6:
			k5 = k5+5
			paths.append(1)
		else:
			w0 = 6/5
			k5 = k5-7
			paths.append(2)
		if k5 < 3:
			x = x*1
			x = x-9
			paths.append(3)
		else:
			k5 = x+w0
			k5 = 0/w0
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		x = k5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))