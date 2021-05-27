import numpy as np 

def function(x):

	o6 = 7
	w4 = 1
	paths = []
	try:
		if w4 <= 3:
			o6 = o6-0
			o6 = o6-x
			paths.append(1)
		else:
			x = 9/x
			x = x/1
			o6 = o6-5
			paths.append(2)
		if o6 >= 9:
			x = x*0
			paths.append(3)
		else:
			x = o6*1
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))