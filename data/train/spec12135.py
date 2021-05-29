import numpy as np 

def function(x):

	v1 = 5
	w6 = x
	paths = []
	try:
		if x < 8:
			x = w6/x
			x = x+5
			w6 = 6-w6
			paths.append(1)
		else:
			x = 0*9
			x = w6-0
			v1 = v1-7
			paths.append(2)
		if w6 > 6:
			x = x-x
			x = v1*x
			x = x-5
			paths.append(3)
		else:
			v1 = v1-0
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))