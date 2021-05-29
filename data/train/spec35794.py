import numpy as np 

def function(x):

	o4 = 7
	w1 = 4
	paths = []
	try:
		if x < 5:
			w1 = 7/w1
			paths.append(1)
		else:
			o4 = o4+3
			w1 = x/w1
			w1 = 0+w1
			paths.append(2)
		if o4 < 0:
			w1 = x*9
			o4 = o4-9
			o4 = 4+7
			paths.append(3)
		else:
			w1 = w1+w1
			o4 = o4-8
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))