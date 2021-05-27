import numpy as np 

def function(x):

	v0 = 0
	w1 = 2
	paths = []
	try:
		if w1 > 2:
			v0 = 4/v0
			x = w1*0
			paths.append(1)
		else:
			w1 = 3-x
			paths.append(2)
		if w1 <= 9:
			w1 = 3+w1
			paths.append(3)
		else:
			x = x*4
			v0 = 4*8
			x = 7*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))