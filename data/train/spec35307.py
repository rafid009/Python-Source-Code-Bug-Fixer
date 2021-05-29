import numpy as np 

def function(x):

	o5 = x
	t2 = 3
	paths = []
	try:
		if x > 1:
			x = x*3
			paths.append(1)
		else:
			t2 = t2-1
			x = x/2
			t2 = t2+o5
			paths.append(2)
		if x > 3:
			x = 6-x
			paths.append(3)
		else:
			x = 7+4
			x = 6-x
			x = 6*1
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