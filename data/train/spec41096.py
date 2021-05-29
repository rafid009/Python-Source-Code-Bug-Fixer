import numpy as np 

def function(x):

	v0 = 8
	w7 = x
	paths = []
	try:
		if w7 >= 4:
			w7 = 6+2
			v0 = 8*v0
			paths.append(1)
		else:
			w7 = w7+1
			paths.append(2)
		if v0 >= 6:
			x = 2-6
			v0 = v0*w7
			paths.append(3)
		else:
			v0 = 6/w7
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		v0 = v0**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))