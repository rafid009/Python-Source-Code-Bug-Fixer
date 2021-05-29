import numpy as np 

def function(x):

	w0 = 7
	j2 = 7
	paths = []
	try:
		if w0 >= 1:
			w0 = j2*w0
			j2 = 9/j2
			paths.append(1)
		else:
			x = 5/3
			x = 5+1
			j2 = j2-6
			paths.append(2)
		if w0 < 3:
			j2 = w0/j2
			w0 = w0+6
			paths.append(3)
		else:
			x = x-x
			w0 = x-j2
			x = 0+4
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		j2 = w0**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))