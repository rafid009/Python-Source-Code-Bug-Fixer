import numpy as np 

def function(x):

	k1 = x
	w9 = x
	paths = []
	try:
		if k1 <= 2:
			w9 = 2/w9
			k1 = k1/7
			paths.append(1)
		else:
			k1 = k1-3
			paths.append(2)
		if k1 < 8:
			k1 = x/k1
			k1 = 4/k1
			k1 = 8-0
			paths.append(3)
		else:
			x = 3+k1
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		w9 = w9**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))