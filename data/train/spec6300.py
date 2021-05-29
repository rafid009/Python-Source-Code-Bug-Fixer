import numpy as np 

def function(x):

	j6 = x
	w8 = 9
	paths = []
	try:
		if w8 < 4:
			x = x-x
			paths.append(1)
		else:
			w8 = w8*j6
			paths.append(2)
		if x > 1:
			j6 = 5+6
			x = 2+x
			x = j6+w8
			paths.append(3)
		else:
			j6 = 8-j6
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))