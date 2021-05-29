import numpy as np 

def function(x):

	o9 = 6
	o2 = 1
	paths = []
	try:
		if x < 3:
			o9 = o9*x
			x = 5-x
			o2 = x*o2
			paths.append(1)
		else:
			o2 = 7+8
			o9 = o9/9
			paths.append(2)
		if x >= 0:
			x = 2-x
			o9 = o2-6
			x = 9*6
			paths.append(3)
		else:
			x = 6+8
			o2 = o2-x
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o2 = o9**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))