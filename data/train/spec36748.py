import numpy as np 

def function(x):

	a7 = 3
	j2 = x
	paths = []
	try:
		if x >= 7:
			j2 = 4*j2
			paths.append(1)
		else:
			j2 = 2-a7
			a7 = 9+9
			paths.append(2)
		if a7 <= 5:
			a7 = a7+a7
			j2 = j2/j2
			paths.append(3)
		else:
			a7 = 5-1
			j2 = j2*x
			a7 = a7*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))