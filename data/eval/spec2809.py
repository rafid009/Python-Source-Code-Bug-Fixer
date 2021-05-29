import numpy as np 

def function(x):

	w5 = x
	k5 = 8
	paths = []
	try:
		if x > 4:
			x = x/7
			x = 6+k5
			paths.append(1)
		else:
			k5 = 0/8
			paths.append(2)
		if k5 >= 8:
			x = 9+x
			k5 = 7+k5
			paths.append(3)
		else:
			w5 = 4*w5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w5 = w5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))