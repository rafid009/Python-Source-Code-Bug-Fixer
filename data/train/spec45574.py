import numpy as np 

def function(x):

	r5 = 7
	w7 = x
	paths = []
	try:
		if r5 > 8:
			w7 = w7-9
			paths.append(1)
		else:
			w7 = w7*7
			x = x-x
			x = 5+x
			paths.append(2)
		if r5 < 4:
			r5 = r5+1
			r5 = 5+r5
			paths.append(3)
		else:
			r5 = 7*4
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		w7 = w7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))