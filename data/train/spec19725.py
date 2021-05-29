import numpy as np 

def function(x):

	w5 = x
	v5 = 6
	paths = []
	try:
		if w5 > 7:
			x = x/8
			paths.append(1)
		else:
			w5 = w5+x
			v5 = v5+v5
			v5 = v5*v5
			paths.append(2)
		if v5 > 5:
			w5 = 3-x
			paths.append(3)
		else:
			v5 = 3-w5
			w5 = w5-4
			w5 = 2*w5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		v5 = w5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))