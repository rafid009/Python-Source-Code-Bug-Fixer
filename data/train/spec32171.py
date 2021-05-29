import numpy as np 

def function(x):

	w5 = x
	i6 = x
	paths = []
	try:
		if i6 <= 6:
			i6 = i6/5
			paths.append(1)
		else:
			i6 = w5+1
			paths.append(2)
		if i6 > 8:
			x = i6/x
			x = w5*3
			w5 = i6*w5
			paths.append(3)
		else:
			i6 = 7-i6
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))