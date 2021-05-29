import numpy as np 

def function(x):

	w5 = x
	o8 = x
	paths = []
	try:
		if x > 7:
			o8 = o8+7
			o8 = w5/o8
			x = x-9
			paths.append(1)
		else:
			x = 0*2
			x = 9*2
			x = x+7
			paths.append(2)
		if o8 >= 3:
			w5 = w5+9
			o8 = o8+x
			paths.append(3)
		else:
			x = w5+x
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		o8 = w5**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))