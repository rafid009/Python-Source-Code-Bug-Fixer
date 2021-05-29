import numpy as np 

def function(x):

	w5 = x
	v0 = 6
	x = 5
	paths = []
	try:
		if w5 >= 2:
			w5 = 8-w5
			v0 = w5*9
			v0 = v0-1
			paths.append(1)
		else:
			x = x-7
			v0 = 7*1
			w5 = v0-w5
			paths.append(2)
		if v0 <= 4:
			v0 = v0+x
			paths.append(3)
		else:
			w5 = 5-w5
			w5 = w5-9
			v0 = 2/v0
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x = w5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))