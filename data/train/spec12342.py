import numpy as np 

def function(x):

	j2 = 2
	w3 = 8
	paths = []
	try:
		if x > 8:
			w3 = w3*4
			paths.append(1)
		else:
			j2 = j2/j2
			x = x+x
			paths.append(2)
		if j2 > 1:
			x = 1+3
			x = 6/x
			x = j2/w3
			paths.append(3)
		else:
			w3 = j2+1
			w3 = 3-w3
			w3 = w3/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))