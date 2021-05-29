import numpy as np 

def function(x):

	w8 = x
	i6 = x
	x = x
	paths = []
	try:
		if x < 8:
			i6 = i6*x
			i6 = i6*w8
			paths.append(1)
		else:
			i6 = 7-i6
			paths.append(2)
		if w8 <= 1:
			i6 = 9*i6
			i6 = i6+0
			i6 = 0+i6
			paths.append(3)
		else:
			w8 = 7*5
			w8 = 7/w8
			i6 = x-9
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))