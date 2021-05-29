import numpy as np 

def function(x):

	j5 = x
	f6 = x
	paths = []
	try:
		if x > 2:
			f6 = j5*5
			x = x/8
			f6 = f6+x
			paths.append(1)
		else:
			f6 = f6*f6
			f6 = 1-f6
			f6 = f6-f6
			paths.append(2)
		if j5 >= 0:
			f6 = f6+9
			x = x/8
			paths.append(3)
		else:
			j5 = j5*f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))