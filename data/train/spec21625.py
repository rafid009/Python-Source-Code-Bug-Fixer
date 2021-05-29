import numpy as np 

def function(x):

	v3 = 0
	w5 = x
	paths = []
	try:
		if v3 >= 0:
			v3 = 5-v3
			v3 = v3*6
			paths.append(1)
		else:
			x = x/8
			w5 = w5-x
			paths.append(2)
		if v3 > 6:
			x = w5*x
			v3 = v3*1
			paths.append(3)
		else:
			v3 = v3/1
			w5 = 9+9
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w5 = w5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))