import numpy as np 

def function(x):

	f4 = 3
	n9 = 2
	paths = []
	try:
		if f4 <= 5:
			n9 = 3+n9
			f4 = f4+3
			paths.append(1)
		else:
			n9 = 3*f4
			n9 = 9-n9
			f4 = 6+f4
			paths.append(2)
		if x < 5:
			x = x/1
			f4 = x-5
			paths.append(3)
		else:
			x = x*3
			x = x/f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))