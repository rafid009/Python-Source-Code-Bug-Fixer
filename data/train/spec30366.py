import numpy as np 

def function(x):

	j2 = x
	w7 = x
	paths = []
	try:
		if x <= 8:
			w7 = 8*w7
			x = 3+x
			w7 = w7+1
			paths.append(1)
		else:
			j2 = w7/j2
			paths.append(2)
		if x >= 2:
			j2 = 5*x
			paths.append(3)
		else:
			j2 = j2+0
			x = 8+j2
			w7 = w7+5
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		w7 = j2**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))