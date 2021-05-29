import numpy as np 

def function(x):

	o9 = x
	w4 = x
	paths = []
	try:
		if o9 > 1:
			x = 5/x
			paths.append(1)
		else:
			x = x+w4
			x = x*0
			paths.append(2)
		if o9 > 5:
			x = x-4
			x = x/6
			o9 = 4-x
			paths.append(3)
		else:
			w4 = 5*w4
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		w4 = o9**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))