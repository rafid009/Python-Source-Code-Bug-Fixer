import numpy as np 

def function(x):

	l4 = x
	o5 = 4
	paths = []
	try:
		if x < 6:
			o5 = o5*9
			o5 = o5+2
			o5 = x-7
			paths.append(1)
		else:
			x = 6+x
			l4 = l4-1
			o5 = o5*9
			paths.append(2)
		if l4 >= 0:
			l4 = 0/l4
			x = 3-o5
			x = l4*3
			paths.append(3)
		else:
			l4 = x/1
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