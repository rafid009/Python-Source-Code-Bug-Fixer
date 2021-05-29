import numpy as np 

def function(x):

	l5 = x
	o8 = x
	paths = []
	try:
		if o8 < 3:
			o8 = o8+l5
			l5 = 7+l5
			l5 = l5*l5
			paths.append(1)
		else:
			o8 = 3-o8
			x = x+x
			paths.append(2)
		if x <= 0:
			x = x-2
			l5 = 8/8
			paths.append(3)
		else:
			o8 = 2+5
			x = 7*8
			x = l5+0
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))