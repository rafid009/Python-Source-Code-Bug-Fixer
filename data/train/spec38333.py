import numpy as np 

def function(x):

	j4 = 7
	w3 = x
	paths = []
	try:
		if j4 >= 4:
			w3 = w3+6
			j4 = j4-0
			x = x-1
			paths.append(1)
		else:
			j4 = j4*2
			paths.append(2)
		if w3 <= 0:
			w3 = w3*9
			j4 = 5-7
			paths.append(3)
		else:
			x = 3-j4
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		w3 = j4**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))