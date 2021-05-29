import numpy as np 

def function(x):

	t0 = x
	j7 = 7
	paths = []
	try:
		if x >= 0:
			t0 = 5*t0
			t0 = t0+j7
			paths.append(1)
		else:
			x = 4+j7
			paths.append(2)
		if j7 <= 1:
			t0 = 6+t0
			t0 = j7-7
			paths.append(3)
		else:
			t0 = t0+5
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		j7 = t0**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))