import numpy as np 

def function(x):

	t6 = 8
	j4 = 6
	paths = []
	try:
		if j4 > 0:
			j4 = 9*j4
			paths.append(1)
		else:
			t6 = 8-t6
			t6 = t6-9
			x = t6+x
			paths.append(2)
		if j4 <= 5:
			x = 3/x
			x = x/t6
			j4 = 2/j4
			paths.append(3)
		else:
			j4 = j4-0
			t6 = t6*0
			t6 = j4+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))