import numpy as np 

def function(x):

	d1 = 4
	v5 = x
	paths = []
	try:
		if d1 < 4:
			d1 = x/3
			paths.append(1)
		else:
			v5 = v5/d1
			paths.append(2)
		if d1 >= 8:
			x = d1-1
			d1 = 1-d1
			x = d1+2
			paths.append(3)
		else:
			v5 = 9-v5
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))