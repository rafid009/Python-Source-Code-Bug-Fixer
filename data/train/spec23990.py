import numpy as np 

def function(x):

	d7 = x
	v5 = x
	paths = []
	try:
		if x < 8:
			d7 = d7+x
			x = 5/x
			x = 0/x
			paths.append(1)
		else:
			d7 = x-7
			x = x-0
			d7 = 7*v5
			paths.append(2)
		if d7 < 2:
			v5 = 6-v5
			d7 = d7*3
			x = 2-x
			paths.append(3)
		else:
			x = x/2
			v5 = v5/9
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		v5 = d7**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))