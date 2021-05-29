import numpy as np 

def function(x):

	v6 = 0
	w5 = x
	paths = []
	try:
		if x < 4:
			w5 = 7+8
			x = x-6
			v6 = x*4
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if x <= 2:
			w5 = 6*w5
			x = 2*x
			paths.append(3)
		else:
			v6 = x*v6
			v6 = v6*v6
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		w5 = v6**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))