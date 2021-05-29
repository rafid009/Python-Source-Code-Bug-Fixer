import numpy as np 

def function(x):

	j1 = x
	t3 = 8
	x = x
	paths = []
	try:
		if t3 < 8:
			x = 7/x
			x = x*0
			paths.append(1)
		else:
			t3 = 5+4
			paths.append(2)
		if x > 4:
			t3 = x-t3
			j1 = 5+j1
			paths.append(3)
		else:
			j1 = 4-j1
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))