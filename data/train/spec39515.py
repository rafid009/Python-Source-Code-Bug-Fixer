import numpy as np 

def function(x):

	o5 = x
	n7 = 0
	x = 6
	paths = []
	try:
		if n7 >= 6:
			x = 9/x
			paths.append(1)
		else:
			o5 = 0/1
			x = x/x
			paths.append(2)
		if x < 7:
			n7 = n7+x
			n7 = n7-2
			x = x*o5
			paths.append(3)
		else:
			o5 = 3-o5
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		o5 = n7**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))