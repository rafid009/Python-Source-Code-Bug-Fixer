import numpy as np 

def function(x):

	w2 = x
	v0 = 2
	x = 6
	paths = []
	try:
		if v0 > 0:
			v0 = 4-5
			paths.append(1)
		else:
			x = v0*3
			v0 = w2/w2
			paths.append(2)
		if v0 < 7:
			v0 = v0*w2
			v0 = v0/7
			w2 = x*w2
			paths.append(3)
		else:
			w2 = 4+v0
			w2 = w2/x
			v0 = v0-9
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))