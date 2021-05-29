import numpy as np 

def function(x):

	o5 = 7
	w6 = x
	paths = []
	try:
		if w6 > 7:
			w6 = 1*0
			w6 = w6/o5
			paths.append(1)
		else:
			x = x*7
			o5 = 5/o5
			paths.append(2)
		if x <= 1:
			o5 = o5+4
			o5 = 4/o5
			o5 = 2*o5
			paths.append(3)
		else:
			o5 = o5-o5
			o5 = o5-4
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		w6 = o5**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))