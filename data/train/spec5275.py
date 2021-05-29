import numpy as np 

def function(x):

	f4 = 4
	o2 = 6
	paths = []
	try:
		if x > 0:
			f4 = f4+f4
			x = x+4
			paths.append(1)
		else:
			f4 = o2/f4
			paths.append(2)
		if f4 > 5:
			x = x/4
			x = x+0
			paths.append(3)
		else:
			f4 = f4/x
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