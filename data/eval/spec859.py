import numpy as np 

def function(x):

	r7 = x
	w7 = x
	paths = []
	try:
		if r7 >= 7:
			r7 = 2/6
			paths.append(1)
		else:
			r7 = r7/6
			r7 = r7+0
			paths.append(2)
		if r7 <= 8:
			r7 = w7+w7
			paths.append(3)
		else:
			r7 = r7/1
			w7 = w7*2
			w7 = 9/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))