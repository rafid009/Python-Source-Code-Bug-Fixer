import numpy as np 

def function(x):

	j2 = x
	j5 = x
	paths = []
	try:
		if j5 < 2:
			j5 = j5/5
			paths.append(1)
		else:
			j2 = j2+9
			paths.append(2)
		if j5 <= 1:
			j5 = j5*j5
			j2 = 4+j2
			paths.append(3)
		else:
			j2 = j2-0
			j2 = 5/j2
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))