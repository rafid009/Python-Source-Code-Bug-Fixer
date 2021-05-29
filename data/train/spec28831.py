import numpy as np 

def function(x):

	i4 = x
	r1 = x
	paths = []
	try:
		if i4 <= 4:
			r1 = r1+6
			i4 = i4*x
			paths.append(1)
		else:
			i4 = i4/8
			paths.append(2)
		if x < 2:
			x = i4*9
			paths.append(3)
		else:
			r1 = r1+3
			i4 = i4*6
			r1 = r1/2
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))