import numpy as np 

def function(x):

	i9 = 2
	w2 = x
	paths = []
	try:
		if i9 < 5:
			x = 6-x
			w2 = i9-4
			paths.append(1)
		else:
			x = x-4
			w2 = 7-w2
			paths.append(2)
		if x < 8:
			w2 = 5-6
			i9 = i9*i9
			w2 = x*0
			paths.append(3)
		else:
			i9 = 6-i9
			x = 9+7
			i9 = i9+4
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))