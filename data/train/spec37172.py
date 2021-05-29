import numpy as np 

def function(x):

	o9 = x
	w6 = x
	x = 6
	paths = []
	try:
		if o9 <= 6:
			o9 = 2*7
			x = x*o9
			x = x+1
			paths.append(1)
		else:
			x = x*x
			w6 = w6+7
			paths.append(2)
		if w6 < 1:
			x = 2+3
			o9 = o9/x
			x = x*3
			paths.append(3)
		else:
			x = w6/w6
			o9 = 8/3
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))