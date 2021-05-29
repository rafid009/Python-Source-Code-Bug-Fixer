import numpy as np 

def function(x):

	j7 = 9
	t6 = 4
	paths = []
	try:
		if x > 4:
			j7 = x*9
			x = x/1
			paths.append(1)
		else:
			t6 = 3-2
			t6 = t6+5
			paths.append(2)
		if t6 > 2:
			t6 = x/x
			j7 = x+x
			x = x-3
			paths.append(3)
		else:
			x = j7/6
			j7 = 6/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))