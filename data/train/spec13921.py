import numpy as np 

def function(x):

	w5 = x
	v3 = 2
	paths = []
	try:
		if v3 > 7:
			w5 = w5*w5
			w5 = v3+2
			paths.append(1)
		else:
			v3 = 2-9
			paths.append(2)
		if x < 0:
			x = 8+x
			paths.append(3)
		else:
			x = x+5
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