import numpy as np 

def function(x):

	a2 = 1
	j2 = 5
	paths = []
	try:
		if a2 <= 0:
			a2 = a2*4
			paths.append(1)
		else:
			x = 5*9
			a2 = 2-a2
			j2 = j2-8
			paths.append(2)
		if j2 < 3:
			a2 = a2-3
			paths.append(3)
		else:
			a2 = 6-a2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		j2 = a2**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))