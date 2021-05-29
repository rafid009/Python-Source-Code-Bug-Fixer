import numpy as np 

def function(x):

	r2 = 8
	j2 = x
	paths = []
	try:
		if j2 > 7:
			j2 = 7-j2
			r2 = 4+4
			j2 = x+j2
			paths.append(1)
		else:
			r2 = 1-2
			paths.append(2)
		if x <= 2:
			r2 = 2-9
			paths.append(3)
		else:
			j2 = 7/8
			r2 = r2-5
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))