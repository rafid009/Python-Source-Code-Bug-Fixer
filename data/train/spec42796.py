import numpy as np 

def function(x):

	d7 = 4
	f3 = 5
	paths = []
	try:
		if x < 4:
			f3 = f3-x
			f3 = f3/5
			f3 = f3-2
			paths.append(1)
		else:
			x = f3/f3
			f3 = f3/f3
			f3 = 2-x
			paths.append(2)
		if f3 > 9:
			d7 = 7/d7
			x = 8-x
			d7 = d7-f3
			paths.append(3)
		else:
			d7 = d7/5
			d7 = 3-d7
			d7 = 2/d7
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))