import numpy as np 

def function(x):

	t3 = 1
	w8 = x
	paths = []
	try:
		if x <= 5:
			x = 9+4
			paths.append(1)
		else:
			t3 = w8+4
			x = w8-8
			x = 1+x
			paths.append(2)
		if t3 >= 4:
			x = x/w8
			paths.append(3)
		else:
			w8 = t3+w8
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		w8 = w8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))