import numpy as np 

def function(x):

	w5 = x
	x2 = x
	x = 4
	paths = []
	try:
		if x2 < 4:
			x = 8+x
			w5 = 5-x2
			w5 = 1+w5
			paths.append(1)
		else:
			w5 = 5*6
			paths.append(2)
		if w5 <= 9:
			w5 = w5/8
			w5 = 1*0
			paths.append(3)
		else:
			x = x2-w5
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		w5 = x2**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))