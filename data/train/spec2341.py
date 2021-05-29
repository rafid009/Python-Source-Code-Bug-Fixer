import numpy as np 

def function(x):

	w5 = 4
	v9 = x
	paths = []
	try:
		if v9 >= 8:
			x = 0-w5
			w5 = 2-w5
			w5 = 3*w5
			paths.append(1)
		else:
			v9 = 2*v9
			w5 = w5/8
			w5 = 1-w5
			paths.append(2)
		if x > 4:
			v9 = w5+w5
			w5 = w5+9
			paths.append(3)
		else:
			x = x-3
			w5 = 4+w5
			w5 = w5*w5
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		v9 = v9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))