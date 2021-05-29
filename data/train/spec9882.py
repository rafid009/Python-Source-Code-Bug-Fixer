import numpy as np 

def function(x):

	o7 = 6
	m7 = 8
	x = x
	paths = []
	try:
		if m7 < 3:
			o7 = 6-o7
			x = x-x
			o7 = o7*3
			paths.append(1)
		else:
			o7 = 3/o7
			o7 = o7+x
			x = o7/x
			paths.append(2)
		if o7 <= 7:
			x = x-8
			x = x/7
			paths.append(3)
		else:
			x = 2-x
			o7 = m7+o7
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		o7 = o7**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))