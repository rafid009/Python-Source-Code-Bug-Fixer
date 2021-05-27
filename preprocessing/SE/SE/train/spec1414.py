import numpy as np 

def function(x):

	a1 = x
	j2 = 8
	paths = []
	try:
		if j2 > 6:
			x = a1-4
			paths.append(1)
		else:
			j2 = j2/1
			j2 = j2/7
			a1 = 8/2
			paths.append(2)
		if a1 <= 4:
			j2 = j2/a1
			paths.append(3)
		else:
			x = j2-a1
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		a1 = j2**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))