import numpy as np 

def function(x):

	d1 = x
	s1 = x
	x = x
	paths = []
	try:
		if d1 <= 0:
			x = s1-x
			paths.append(1)
		else:
			x = 5/5
			x = 7+x
			paths.append(2)
		if d1 >= 7:
			x = 4-1
			paths.append(3)
		else:
			d1 = s1-d1
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		d1 = s1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))