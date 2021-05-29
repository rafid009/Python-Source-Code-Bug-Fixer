import numpy as np 

def function(x):

	o6 = 7
	l5 = x
	paths = []
	try:
		if l5 >= 3:
			o6 = l5+9
			l5 = x/9
			paths.append(1)
		else:
			l5 = l5*1
			x = 4/3
			x = x-3
			paths.append(2)
		if o6 < 0:
			o6 = 8+x
			l5 = o6-l5
			paths.append(3)
		else:
			o6 = o6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o6 = x**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))