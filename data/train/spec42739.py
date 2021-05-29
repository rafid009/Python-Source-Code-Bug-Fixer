import numpy as np 

def function(x):

	x4 = x
	f2 = x
	paths = []
	try:
		if x < 4:
			x = x*4
			paths.append(1)
		else:
			f2 = 9/f2
			paths.append(2)
		if x > 2:
			f2 = f2*1
			x4 = x4/2
			f2 = x/4
			paths.append(3)
		else:
			x4 = x4+9
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		f2 = x4**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))