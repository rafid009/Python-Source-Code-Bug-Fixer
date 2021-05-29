import numpy as np 

def function(x):

	t4 = 9
	w3 = 7
	paths = []
	try:
		if t4 >= 1:
			t4 = t4-7
			w3 = x+w3
			w3 = 8+w3
			paths.append(1)
		else:
			x = x/4
			w3 = x-x
			w3 = w3-4
			paths.append(2)
		if t4 <= 3:
			t4 = t4/5
			paths.append(3)
		else:
			x = 1*t4
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