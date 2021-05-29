import numpy as np 

def function(x):

	w1 = x
	k9 = 6
	paths = []
	try:
		if x < 1:
			w1 = w1+2
			paths.append(1)
		else:
			w1 = x/1
			paths.append(2)
		if w1 <= 0:
			x = w1-x
			x = x/1
			w1 = 3/w1
			paths.append(3)
		else:
			k9 = k9+1
			x = 6+x
			k9 = k9+4
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))