import numpy as np 

def function(x):

	t1 = x
	v1 = x
	paths = []
	try:
		if x <= 1:
			t1 = t1+6
			v1 = v1-2
			paths.append(1)
		else:
			x = 7/x
			t1 = t1-x
			t1 = v1-9
			paths.append(2)
		if t1 > 5:
			t1 = t1*4
			paths.append(3)
		else:
			t1 = 1/t1
			x = x+4
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		v1 = t1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))