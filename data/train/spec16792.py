import numpy as np 

def function(x):

	i7 = x
	w2 = 4
	paths = []
	try:
		if i7 <= 6:
			x = 8+3
			paths.append(1)
		else:
			x = 0-i7
			i7 = 8-1
			paths.append(2)
		if i7 < 1:
			x = x*4
			paths.append(3)
		else:
			x = x*x
			i7 = 0/i7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		w2 = i7**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))