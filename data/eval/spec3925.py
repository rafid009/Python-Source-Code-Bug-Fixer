import numpy as np 

def function(x):

	j2 = x
	e1 = 0
	paths = []
	try:
		if e1 <= 1:
			x = 7+x
			j2 = x/j2
			paths.append(1)
		else:
			e1 = e1+x
			x = 1-j2
			paths.append(2)
		if j2 >= 2:
			x = 8/x
			x = j2+6
			paths.append(3)
		else:
			j2 = j2-e1
			x = x/2
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