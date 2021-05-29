import numpy as np 

def function(x):

	u3 = 9
	j0 = 5
	paths = []
	try:
		if j0 >= 3:
			u3 = u3*x
			j0 = 6+j0
			x = x/j0
			paths.append(1)
		else:
			u3 = j0*u3
			j0 = j0/9
			paths.append(2)
		if x > 1:
			u3 = u3-8
			x = x+x
			paths.append(3)
		else:
			j0 = j0/9
			x = x-1
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))