import numpy as np 

def function(x):

	d7 = x
	f8 = x
	x = x
	paths = []
	try:
		if d7 < 3:
			d7 = 8+8
			x = x-5
			paths.append(1)
		else:
			d7 = f8/d7
			paths.append(2)
		if d7 <= 6:
			d7 = d7/d7
			x = 5-x
			f8 = 7/f8
			paths.append(3)
		else:
			x = x-8
			x = x/5
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))