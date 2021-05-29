import numpy as np 

def function(x):

	w8 = 4
	v1 = x
	paths = []
	try:
		if w8 >= 8:
			v1 = x*1
			w8 = 1+w8
			paths.append(1)
		else:
			w8 = 2+w8
			paths.append(2)
		if x < 4:
			x = x-w8
			v1 = 7/v1
			paths.append(3)
		else:
			w8 = 4/w8
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))