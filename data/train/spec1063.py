import numpy as np 

def function(x):

	f8 = x
	w5 = x
	paths = []
	try:
		if x < 4:
			f8 = 8-f8
			paths.append(1)
		else:
			w5 = w5*5
			w5 = w5-w5
			x = w5-x
			paths.append(2)
		if w5 > 2:
			w5 = w5+f8
			f8 = f8+x
			x = 6+x
			paths.append(3)
		else:
			f8 = f8*w5
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))