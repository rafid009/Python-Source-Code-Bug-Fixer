import numpy as np 

def function(x):

	o1 = 5
	v3 = x
	paths = []
	try:
		if v3 < 3:
			o1 = 0/v3
			paths.append(1)
		else:
			v3 = 5*4
			v3 = 7-0
			paths.append(2)
		if o1 <= 2:
			x = x+o1
			paths.append(3)
		else:
			x = x+8
			x = 6*v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))