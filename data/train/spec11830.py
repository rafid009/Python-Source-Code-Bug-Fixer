import numpy as np 

def function(x):

	w6 = x
	o0 = x
	paths = []
	try:
		if o0 <= 9:
			w6 = 0-w6
			x = 6*x
			x = x-2
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if x <= 5:
			x = x-2
			paths.append(3)
		else:
			o0 = 5*0
			w6 = w6-0
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		w6 = o0**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))