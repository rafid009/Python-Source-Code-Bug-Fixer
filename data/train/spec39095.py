import numpy as np 

def function(x):

	v4 = x
	f7 = x
	paths = []
	try:
		if x < 3:
			f7 = f7/9
			v4 = v4/8
			f7 = x-f7
			paths.append(1)
		else:
			x = 6-6
			f7 = 2+v4
			v4 = v4/v4
			paths.append(2)
		if f7 <= 4:
			v4 = 8/v4
			f7 = f7*x
			f7 = 6-0
			paths.append(3)
		else:
			v4 = x/6
			v4 = v4+v4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))