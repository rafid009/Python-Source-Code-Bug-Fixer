import numpy as np 

def function(x):

	w6 = x
	x8 = x
	x = 9
	paths = []
	try:
		if x8 <= 7:
			w6 = w6-2
			w6 = 7+w6
			x8 = 7-x
			paths.append(1)
		else:
			w6 = 8-x
			x = 9-3
			w6 = 6-x8
			paths.append(2)
		if w6 > 8:
			x8 = x8+4
			x = x/x
			paths.append(3)
		else:
			w6 = w6-0
			w6 = w6+8
			w6 = w6*0
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		w6 = x8**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))