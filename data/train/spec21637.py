import numpy as np 

def function(x):

	j0 = x
	t1 = 5
	x = 8
	paths = []
	try:
		if t1 <= 5:
			t1 = 9-j0
			t1 = t1-x
			x = j0*t1
			paths.append(1)
		else:
			x = 1-x
			paths.append(2)
		if x >= 0:
			j0 = 8+j0
			paths.append(3)
		else:
			j0 = 9/3
			x = x+1
			t1 = t1+t1
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))