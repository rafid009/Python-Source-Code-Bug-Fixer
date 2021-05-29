import numpy as np 

def function(x):

	v6 = x
	w4 = x
	paths = []
	try:
		if x > 0:
			x = x+w4
			x = x/w4
			paths.append(1)
		else:
			w4 = w4-x
			x = x-7
			paths.append(2)
		if v6 <= 6:
			x = 2+3
			paths.append(3)
		else:
			x = x/w4
			x = 6*w4
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))