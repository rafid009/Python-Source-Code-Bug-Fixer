import numpy as np 

def function(x):

	v4 = 9
	r1 = 4
	paths = []
	try:
		if v4 > 1:
			x = x+9
			r1 = r1-5
			paths.append(1)
		else:
			r1 = r1/8
			paths.append(2)
		if v4 <= 6:
			v4 = 7*8
			paths.append(3)
		else:
			x = 7*x
			x = x/6
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		v4 = r1**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))