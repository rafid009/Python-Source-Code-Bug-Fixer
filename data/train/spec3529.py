import numpy as np 

def function(x):

	d6 = x
	f7 = x
	paths = []
	try:
		if x < 4:
			d6 = 6/d6
			f7 = x*3
			paths.append(1)
		else:
			f7 = f7/d6
			d6 = f7-x
			paths.append(2)
		if f7 >= 2:
			d6 = 3+0
			x = f7*5
			f7 = f7/d6
			paths.append(3)
		else:
			f7 = 7-2
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		f7 = d6**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))