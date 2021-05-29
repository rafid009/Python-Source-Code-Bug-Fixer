import numpy as np 

def function(x):

	w3 = x
	t4 = 1
	paths = []
	try:
		if x <= 1:
			x = 6/x
			w3 = t4*7
			paths.append(1)
		else:
			w3 = x/x
			w3 = w3-6
			paths.append(2)
		if w3 >= 7:
			t4 = 6/t4
			w3 = w3/t4
			paths.append(3)
		else:
			x = t4/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))