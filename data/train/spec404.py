import numpy as np 

def function(x):

	r7 = 9
	j2 = x
	paths = []
	try:
		if x > 7:
			x = 6/j2
			r7 = r7*3
			r7 = r7/x
			paths.append(1)
		else:
			r7 = 1-9
			paths.append(2)
		if j2 < 6:
			x = j2/8
			j2 = j2-3
			paths.append(3)
		else:
			j2 = j2-6
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