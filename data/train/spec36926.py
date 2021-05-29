import numpy as np 

def function(x):

	b7 = 0
	j5 = x
	paths = []
	try:
		if b7 > 3:
			x = x/x
			paths.append(1)
		else:
			j5 = j5-7
			paths.append(2)
		if x > 0:
			j5 = j5-j5
			paths.append(3)
		else:
			j5 = j5*2
			b7 = 3*2
			j5 = b7+9
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