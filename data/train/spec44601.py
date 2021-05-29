import numpy as np 

def function(x):

	w3 = x
	t5 = x
	paths = []
	try:
		if t5 >= 7:
			w3 = w3-w3
			paths.append(1)
		else:
			w3 = x+0
			paths.append(2)
		if t5 > 7:
			w3 = w3-w3
			paths.append(3)
		else:
			t5 = 7*t5
			t5 = 7+3
			t5 = w3+t5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))