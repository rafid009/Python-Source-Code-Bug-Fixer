import numpy as np 

def function(x):

	j6 = x
	w3 = 1
	paths = []
	try:
		if j6 > 4:
			j6 = 2+j6
			paths.append(1)
		else:
			w3 = 1/w3
			x = 8+w3
			x = 1/9
			paths.append(2)
		if j6 >= 9:
			j6 = j6/5
			w3 = x+x
			w3 = w3-3
			paths.append(3)
		else:
			x = 8/x
			x = 0-x
			w3 = 7-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))