import numpy as np 

def function(x):

	w6 = x
	o2 = x
	paths = []
	try:
		if x > 4:
			w6 = w6-3
			o2 = o2+3
			o2 = o2-7
			paths.append(1)
		else:
			w6 = w6*o2
			o2 = o2/2
			x = x*w6
			paths.append(2)
		if w6 < 5:
			o2 = o2+9
			o2 = o2*o2
			w6 = w6/9
			paths.append(3)
		else:
			w6 = 0-3
			w6 = 0*w6
			w6 = w6+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))