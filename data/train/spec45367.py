import numpy as np 

def function(x):

	j3 = 6
	w3 = 1
	paths = []
	try:
		if j3 > 5:
			j3 = 4-j3
			j3 = j3-0
			w3 = 8-x
			paths.append(1)
		else:
			j3 = j3+x
			j3 = 9+j3
			w3 = w3+7
			paths.append(2)
		if w3 <= 7:
			x = x-8
			w3 = w3+7
			paths.append(3)
		else:
			w3 = w3/w3
			w3 = 3-1
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))