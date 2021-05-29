import numpy as np 

def function(x):

	j9 = 7
	t2 = x
	paths = []
	try:
		if x >= 3:
			j9 = j9+4
			t2 = t2/2
			paths.append(1)
		else:
			x = j9+x
			paths.append(2)
		if x <= 1:
			x = t2-x
			j9 = j9/x
			paths.append(3)
		else:
			j9 = 8+5
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		j9 = t2**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))