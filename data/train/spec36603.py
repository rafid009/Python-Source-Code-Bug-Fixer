import numpy as np 

def function(x):

	r1 = 5
	k4 = x
	paths = []
	try:
		if k4 <= 7:
			k4 = 2+k4
			r1 = r1+2
			paths.append(1)
		else:
			r1 = r1-r1
			x = 2/x
			paths.append(2)
		if k4 < 5:
			k4 = k4-8
			r1 = 9-r1
			x = k4+k4
			paths.append(3)
		else:
			k4 = 3/k4
			r1 = r1-5
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		k4 = r1**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))