import numpy as np 

def function(x):

	v3 = x
	w7 = x
	paths = []
	try:
		if w7 >= 1:
			v3 = v3+v3
			x = 8-v3
			v3 = v3*3
			paths.append(1)
		else:
			w7 = w7*2
			v3 = v3/3
			w7 = w7+9
			paths.append(2)
		if v3 < 0:
			x = 7*x
			x = v3*7
			x = x*w7
			paths.append(3)
		else:
			v3 = 9/4
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		v3 = w7**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))