import numpy as np 

def function(x):

	w1 = x
	v9 = 9
	paths = []
	try:
		if w1 >= 8:
			x = x+9
			w1 = w1/w1
			w1 = 6+1
			paths.append(1)
		else:
			v9 = v9-x
			paths.append(2)
		if w1 > 0:
			v9 = 1+x
			v9 = v9+8
			w1 = w1*x
			paths.append(3)
		else:
			x = x-3
			x = x*w1
			x = 7*v9
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		v9 = w1**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))