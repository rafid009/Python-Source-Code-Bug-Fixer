import numpy as np 

def function(x):

	o9 = x
	q5 = x
	paths = []
	try:
		if o9 < 6:
			o9 = o9-9
			o9 = o9/3
			paths.append(1)
		else:
			o9 = q5/o9
			q5 = x*q5
			q5 = o9+q5
			paths.append(2)
		if x > 3:
			o9 = 6-o9
			paths.append(3)
		else:
			q5 = q5-7
			o9 = 1+o9
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))