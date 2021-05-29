import numpy as np 

def function(x):

	s3 = 1
	t7 = 2
	paths = []
	try:
		if t7 >= 0:
			x = x+t7
			paths.append(1)
		else:
			t7 = t7+4
			s3 = s3+1
			paths.append(2)
		if x < 0:
			x = x+t7
			t7 = t7-1
			paths.append(3)
		else:
			x = 8-t7
			t7 = 4+2
			t7 = 7-t7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))