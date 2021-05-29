import numpy as np 

def function(x):

	t2 = 3
	v1 = x
	paths = []
	try:
		if v1 <= 9:
			x = x-0
			v1 = v1-t2
			t2 = 5*v1
			paths.append(1)
		else:
			v1 = v1/2
			t2 = 2-6
			paths.append(2)
		if v1 > 1:
			v1 = 9/x
			paths.append(3)
		else:
			v1 = v1+3
			t2 = 6-x
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))