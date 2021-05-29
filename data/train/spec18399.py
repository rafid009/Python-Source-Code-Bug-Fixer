import numpy as np 

def function(x):

	a5 = 8
	j2 = 6
	paths = []
	try:
		if j2 >= 4:
			a5 = a5+x
			a5 = a5+8
			paths.append(1)
		else:
			j2 = j2/5
			paths.append(2)
		if j2 <= 4:
			x = j2-6
			x = 3*j2
			a5 = a5+5
			paths.append(3)
		else:
			x = 5-x
			x = 1/j2
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))