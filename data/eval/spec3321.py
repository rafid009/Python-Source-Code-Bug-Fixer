import numpy as np 

def function(x):

	v1 = x
	f0 = x
	paths = []
	try:
		if x <= 2:
			x = x*1
			x = x+f0
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if f0 < 7:
			v1 = 8+7
			f0 = f0-x
			paths.append(3)
		else:
			f0 = f0*6
			x = x-x
			f0 = 6-6
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))