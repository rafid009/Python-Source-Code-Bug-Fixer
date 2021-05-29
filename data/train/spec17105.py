import numpy as np 

def function(x):

	o6 = x
	w6 = x
	paths = []
	try:
		if x < 2:
			o6 = 7+w6
			paths.append(1)
		else:
			w6 = w6*o6
			x = 8+x
			o6 = o6+6
			paths.append(2)
		if w6 < 0:
			x = x*5
			paths.append(3)
		else:
			w6 = x/w6
			w6 = w6+w6
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		o6 = w6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))