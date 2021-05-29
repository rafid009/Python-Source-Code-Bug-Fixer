import numpy as np 

def function(x):

	t1 = 5
	h1 = x
	paths = []
	try:
		if t1 <= 3:
			h1 = 3*3
			paths.append(1)
		else:
			x = 4/x
			paths.append(2)
		if t1 <= 6:
			t1 = 5*t1
			h1 = h1+x
			x = x/h1
			paths.append(3)
		else:
			x = x/4
			h1 = h1+1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))