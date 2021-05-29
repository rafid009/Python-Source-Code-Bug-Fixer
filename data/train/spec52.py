import numpy as np 

def function(x):

	v7 = x
	w1 = 3
	paths = []
	try:
		if w1 >= 8:
			x = v7/3
			v7 = w1*v7
			w1 = w1*v7
			paths.append(1)
		else:
			x = 9-x
			x = 7-x
			x = x+w1
			paths.append(2)
		if w1 <= 5:
			w1 = w1-1
			x = w1*x
			v7 = v7*7
			paths.append(3)
		else:
			x = 5/x
			w1 = 7*w1
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v7 = v7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))