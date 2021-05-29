import numpy as np 

def function(x):

	b2 = 3
	o5 = x
	x = 6
	paths = []
	try:
		if x <= 9:
			o5 = o5*5
			o5 = o5+4
			paths.append(1)
		else:
			o5 = 6/o5
			b2 = b2*3
			x = 6/b2
			paths.append(2)
		if b2 >= 5:
			b2 = 8+o5
			o5 = o5-x
			paths.append(3)
		else:
			o5 = o5-1
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		b2 = o5**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))