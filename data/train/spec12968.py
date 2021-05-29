import numpy as np 

def function(x):

	i6 = 2
	w3 = 1
	paths = []
	try:
		if x > 0:
			i6 = i6-x
			x = 9-x
			paths.append(1)
		else:
			w3 = w3+x
			i6 = i6*x
			w3 = x-w3
			paths.append(2)
		if i6 > 2:
			x = x/9
			w3 = w3/7
			paths.append(3)
		else:
			w3 = 6*w3
			w3 = w3*i6
			i6 = i6-4
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		w3 = i6**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))