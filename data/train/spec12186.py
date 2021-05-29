import numpy as np 

def function(x):

	w2 = x
	k1 = 1
	paths = []
	try:
		if w2 > 7:
			x = w2+k1
			k1 = k1*2
			paths.append(1)
		else:
			k1 = k1-9
			x = x-7
			paths.append(2)
		if w2 > 4:
			k1 = 0*k1
			x = x-9
			k1 = 3-2
			paths.append(3)
		else:
			w2 = 0*w2
			k1 = 3+k1
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x = k1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))