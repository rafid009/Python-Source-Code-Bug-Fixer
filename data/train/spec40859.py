import numpy as np 

def function(x):

	v4 = x
	f6 = x
	paths = []
	try:
		if x <= 3:
			x = x-5
			paths.append(1)
		else:
			v4 = 2+v4
			v4 = 1*x
			v4 = v4-f6
			paths.append(2)
		if f6 < 8:
			x = x+6
			v4 = v4-2
			x = x+x
			paths.append(3)
		else:
			f6 = 4-5
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		f6 = v4**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))