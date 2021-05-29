import numpy as np 

def function(x):

	k6 = x
	f0 = x
	paths = []
	try:
		if x >= 1:
			x = x+9
			k6 = 1*k6
			paths.append(1)
		else:
			k6 = 5*f0
			k6 = k6/8
			f0 = 1/f0
			paths.append(2)
		if f0 >= 3:
			k6 = k6/k6
			f0 = x*5
			paths.append(3)
		else:
			f0 = 1+k6
			k6 = k6-f0
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