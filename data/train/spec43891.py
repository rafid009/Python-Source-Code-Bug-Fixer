import numpy as np 

def function(x):

	u3 = 8
	f0 = x
	paths = []
	try:
		if x >= 1:
			f0 = f0+9
			paths.append(1)
		else:
			u3 = u3*3
			x = x-5
			paths.append(2)
		if u3 < 4:
			f0 = 0+f0
			paths.append(3)
		else:
			x = 1-0
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))