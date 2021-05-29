import numpy as np 

def function(x):

	w7 = x
	k9 = 5
	paths = []
	try:
		if w7 >= 4:
			x = 1-x
			paths.append(1)
		else:
			k9 = 2*6
			paths.append(2)
		if k9 <= 1:
			k9 = k9/5
			w7 = 6-w7
			x = x*2
			paths.append(3)
		else:
			w7 = 6/w7
			w7 = 4*w7
			w7 = 1-4
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		k9 = w7**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))