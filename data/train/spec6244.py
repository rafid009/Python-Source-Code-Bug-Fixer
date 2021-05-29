import numpy as np 

def function(x):

	j5 = 2
	t0 = x
	paths = []
	try:
		if x <= 8:
			x = 1*j5
			j5 = j5+t0
			x = x/4
			paths.append(1)
		else:
			x = x+7
			j5 = 9+7
			t0 = j5*7
			paths.append(2)
		if t0 > 7:
			j5 = x-j5
			j5 = 4*j5
			paths.append(3)
		else:
			t0 = 5*t0
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))