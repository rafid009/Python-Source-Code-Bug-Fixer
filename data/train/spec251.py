import numpy as np 

def function(x):

	v4 = 1
	f8 = x
	paths = []
	try:
		if v4 <= 5:
			f8 = 1-f8
			x = x+1
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if f8 >= 7:
			x = x-x
			x = 8*x
			v4 = x*v4
			paths.append(3)
		else:
			v4 = v4-4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		f8 = v4**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))