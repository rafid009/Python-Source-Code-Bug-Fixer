import numpy as np 

def function(x):

	j5 = 3
	w3 = 9
	paths = []
	try:
		if x >= 6:
			x = x-0
			w3 = 4/w3
			paths.append(1)
		else:
			w3 = 5+w3
			w3 = w3/4
			j5 = 2-7
			paths.append(2)
		if w3 < 3:
			x = x*7
			paths.append(3)
		else:
			w3 = x-w3
			w3 = w3+0
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))