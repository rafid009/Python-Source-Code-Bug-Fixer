import numpy as np 

def function(x):

	l4 = 5
	o5 = x
	paths = []
	try:
		if x <= 9:
			x = 4*l4
			x = x-2
			paths.append(1)
		else:
			l4 = 1/l4
			o5 = 7-9
			l4 = x*0
			paths.append(2)
		if o5 > 6:
			o5 = 3/o5
			l4 = x/8
			paths.append(3)
		else:
			x = 3-x
			x = x-0
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		l4 = o5**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))