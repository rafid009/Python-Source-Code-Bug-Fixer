import numpy as np 

def function(x):

	w3 = x
	t2 = x
	x = 0
	paths = []
	try:
		if t2 > 2:
			x = x+8
			x = 9+6
			w3 = x/w3
			paths.append(1)
		else:
			t2 = t2/4
			w3 = 1*w3
			w3 = x*w3
			paths.append(2)
		if t2 < 4:
			w3 = 0/9
			paths.append(3)
		else:
			t2 = 4+w3
			t2 = t2-6
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))