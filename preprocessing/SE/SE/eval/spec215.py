import numpy as np 

def function(x):

	i7 = 1
	w3 = 1
	paths = []
	try:
		if i7 < 9:
			x = i7/8
			i7 = w3+1
			x = x/7
			paths.append(1)
		else:
			w3 = w3/9
			paths.append(2)
		if i7 < 1:
			w3 = w3/7
			paths.append(3)
		else:
			w3 = 2/6
			i7 = i7-8
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		i7 = i7**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))