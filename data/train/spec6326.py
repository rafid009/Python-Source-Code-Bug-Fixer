import numpy as np 

def function(x):

	t5 = 1
	j1 = 4
	paths = []
	try:
		if j1 <= 2:
			j1 = j1*t5
			j1 = t5-j1
			j1 = j1*j1
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if j1 < 2:
			x = 0+1
			x = 0/x
			x = j1-9
			paths.append(3)
		else:
			t5 = t5-7
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