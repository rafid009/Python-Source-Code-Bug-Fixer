import numpy as np 

def function(x):

	d3 = x
	w8 = 6
	paths = []
	try:
		if w8 <= 0:
			w8 = w8/d3
			x = 2-x
			x = 9/5
			paths.append(1)
		else:
			w8 = w8+w8
			paths.append(2)
		if x < 8:
			w8 = 7*9
			paths.append(3)
		else:
			x = x*0
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		w8 = d3**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))