import numpy as np 

def function(x):

	w8 = 9
	r3 = 7
	paths = []
	try:
		if w8 >= 6:
			r3 = 3/x
			x = w8*3
			paths.append(1)
		else:
			r3 = 5+1
			r3 = 7+6
			r3 = r3/r3
			paths.append(2)
		if r3 <= 4:
			x = x*w8
			paths.append(3)
		else:
			w8 = w8*1
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		w8 = r3**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))