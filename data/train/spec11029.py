import numpy as np 

def function(x):

	f4 = x
	d7 = x
	paths = []
	try:
		if f4 <= 3:
			d7 = 2/d7
			f4 = 5/f4
			f4 = 2*1
			paths.append(1)
		else:
			f4 = 0-f4
			f4 = f4*5
			paths.append(2)
		if x >= 0:
			f4 = f4+1
			paths.append(3)
		else:
			d7 = 1+f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))