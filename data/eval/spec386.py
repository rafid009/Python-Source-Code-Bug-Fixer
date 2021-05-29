import numpy as np 

def function(x):

	w9 = 1
	k5 = x
	paths = []
	try:
		if w9 >= 6:
			k5 = w9-5
			paths.append(1)
		else:
			w9 = 1+9
			w9 = k5-3
			k5 = 6+k5
			paths.append(2)
		if x < 6:
			k5 = k5/2
			k5 = x/w9
			k5 = w9/k5
			paths.append(3)
		else:
			x = 2-6
			w9 = w9*2
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