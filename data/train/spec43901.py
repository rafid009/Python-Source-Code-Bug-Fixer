import numpy as np 

def function(x):

	f0 = 8
	j5 = 9
	paths = []
	try:
		if f0 > 3:
			f0 = f0*f0
			j5 = 3-9
			j5 = 0-0
			paths.append(1)
		else:
			j5 = f0-5
			f0 = f0+x
			paths.append(2)
		if x <= 8:
			j5 = j5-5
			paths.append(3)
		else:
			j5 = 4+j5
			x = x*4
			x = 5+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))