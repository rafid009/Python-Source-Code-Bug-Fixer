import numpy as np 

def function(x):

	j5 = x
	u2 = x
	paths = []
	try:
		if u2 <= 0:
			j5 = x-0
			j5 = 7/j5
			paths.append(1)
		else:
			x = x*0
			u2 = u2/2
			paths.append(2)
		if j5 >= 9:
			j5 = j5+9
			j5 = 0+6
			paths.append(3)
		else:
			x = 3*x
			x = 7-5
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))