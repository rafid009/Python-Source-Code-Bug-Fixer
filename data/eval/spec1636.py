import numpy as np 

def function(x):

	t3 = x
	j9 = x
	paths = []
	try:
		if j9 > 1:
			x = 3*7
			x = x*3
			paths.append(1)
		else:
			j9 = j9*6
			x = 3+6
			x = j9*t3
			paths.append(2)
		if j9 > 2:
			t3 = 8-t3
			t3 = 1+6
			paths.append(3)
		else:
			j9 = 1*j9
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j9 = j9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))