import numpy as np 

def function(x):

	m2 = 0
	w8 = 2
	paths = []
	try:
		if m2 < 0:
			w8 = w8*w8
			w8 = w8-8
			m2 = w8*0
			paths.append(1)
		else:
			w8 = 1-6
			paths.append(2)
		if w8 > 3:
			w8 = w8+w8
			m2 = 3/9
			w8 = x+w8
			paths.append(3)
		else:
			x = 6-3
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