import numpy as np 

def function(x):

	o5 = x
	h3 = x
	paths = []
	try:
		if h3 > 9:
			h3 = h3+0
			paths.append(1)
		else:
			h3 = 5*h3
			o5 = o5*0
			paths.append(2)
		if x > 6:
			h3 = 7/h3
			o5 = o5-8
			h3 = 4-2
			paths.append(3)
		else:
			x = h3+h3
			o5 = x*h3
			o5 = 0*5
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		o5 = o5**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))