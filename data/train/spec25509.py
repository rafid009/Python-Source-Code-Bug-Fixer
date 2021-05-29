import numpy as np 

def function(x):

	d8 = x
	v3 = x
	x = 6
	paths = []
	try:
		if x <= 4:
			v3 = v3/1
			paths.append(1)
		else:
			x = 4-x
			d8 = 8*d8
			paths.append(2)
		if d8 >= 5:
			d8 = d8/1
			paths.append(3)
		else:
			d8 = d8+x
			v3 = v3+1
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