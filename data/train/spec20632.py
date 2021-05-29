import numpy as np 

def function(x):

	d4 = 4
	v7 = x
	x = x
	paths = []
	try:
		if v7 >= 4:
			x = 5-v7
			v7 = v7+6
			x = x-0
			paths.append(1)
		else:
			v7 = v7*2
			x = 2*x
			paths.append(2)
		if d4 > 7:
			d4 = 3/v7
			paths.append(3)
		else:
			v7 = x+v7
			d4 = 2/d4
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		d4 = v7**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))