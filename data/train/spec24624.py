import numpy as np 

def function(x):

	w1 = x
	f4 = 4
	paths = []
	try:
		if w1 >= 8:
			w1 = x*x
			f4 = 5-f4
			f4 = f4*x
			paths.append(1)
		else:
			f4 = w1*4
			paths.append(2)
		if f4 >= 4:
			w1 = 2*5
			w1 = w1-1
			paths.append(3)
		else:
			w1 = 7+w1
			x = 8/2
			w1 = 3/x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))