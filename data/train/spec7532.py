import numpy as np 

def function(x):

	i0 = 7
	w7 = 3
	paths = []
	try:
		if i0 > 9:
			w7 = 4+w7
			i0 = i0/6
			paths.append(1)
		else:
			i0 = w7+w7
			w7 = 0+w7
			x = 2-5
			paths.append(2)
		if x <= 8:
			w7 = x*w7
			paths.append(3)
		else:
			i0 = i0*2
			x = x-x
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		w7 = w7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))