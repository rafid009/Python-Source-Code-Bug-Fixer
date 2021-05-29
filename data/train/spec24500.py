import numpy as np 

def function(x):

	w9 = 3
	d0 = x
	paths = []
	try:
		if x >= 4:
			x = 3/x
			x = x+d0
			paths.append(1)
		else:
			x = x*1
			w9 = 0+w9
			x = d0/3
			paths.append(2)
		if x > 5:
			w9 = w9*w9
			x = d0/x
			paths.append(3)
		else:
			w9 = 9+x
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))