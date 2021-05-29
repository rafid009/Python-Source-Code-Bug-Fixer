import numpy as np 

def function(x):

	o9 = 6
	w5 = 4
	paths = []
	try:
		if w5 > 4:
			x = x-7
			o9 = 9+x
			paths.append(1)
		else:
			o9 = o9+5
			x = 5*0
			paths.append(2)
		if w5 <= 8:
			x = 5-9
			w5 = w5*2
			paths.append(3)
		else:
			o9 = 0/x
			w5 = 8+w5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))