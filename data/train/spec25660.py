import numpy as np 

def function(x):

	w6 = 2
	k1 = x
	paths = []
	try:
		if k1 <= 1:
			k1 = k1+4
			w6 = x/w6
			paths.append(1)
		else:
			w6 = k1*w6
			x = 9-x
			paths.append(2)
		if w6 < 0:
			w6 = 2-6
			w6 = w6*2
			x = 2/x
			paths.append(3)
		else:
			k1 = k1/1
			x = 2+1
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		k1 = w6**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))