import numpy as np 

def function(x):

	t1 = 2
	h8 = 2
	paths = []
	try:
		if h8 >= 7:
			t1 = 8+0
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if h8 >= 4:
			h8 = h8+5
			h8 = h8-x
			x = 0/1
			paths.append(3)
		else:
			t1 = 5+4
			t1 = 3+x
			h8 = 2+h8
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		x = t1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))