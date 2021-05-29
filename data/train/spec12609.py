import numpy as np 

def function(x):

	j2 = 7
	w5 = x
	paths = []
	try:
		if x <= 9:
			j2 = x+w5
			j2 = j2/w5
			paths.append(1)
		else:
			w5 = w5/w5
			x = 6-9
			paths.append(2)
		if x >= 3:
			w5 = 0-x
			paths.append(3)
		else:
			w5 = w5-8
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w5 = w5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))