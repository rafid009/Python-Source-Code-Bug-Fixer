import numpy as np 

def function(x):

	i0 = x
	w5 = x
	x = x
	paths = []
	try:
		if w5 <= 4:
			i0 = i0+9
			x = x/w5
			paths.append(1)
		else:
			x = x/5
			i0 = i0*w5
			paths.append(2)
		if i0 <= 9:
			x = 3-4
			x = x*9
			paths.append(3)
		else:
			w5 = i0-x
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