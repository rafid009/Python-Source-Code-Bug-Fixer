import numpy as np 

def function(x):

	q9 = x
	o5 = 7
	x = 7
	paths = []
	try:
		if o5 < 5:
			q9 = q9+6
			x = o5-9
			q9 = q9-6
			paths.append(1)
		else:
			q9 = o5+x
			paths.append(2)
		if q9 <= 6:
			x = 4/8
			o5 = o5-4
			paths.append(3)
		else:
			x = x/o5
			x = 7+q9
			o5 = 0-4
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