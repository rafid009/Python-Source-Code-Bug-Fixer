import numpy as np 

def function(x):

	t9 = 4
	s3 = x
	paths = []
	try:
		if s3 <= 6:
			s3 = x*4
			t9 = x+s3
			paths.append(1)
		else:
			t9 = t9/4
			paths.append(2)
		if s3 >= 4:
			t9 = 2-t9
			paths.append(3)
		else:
			t9 = s3+x
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		t9 = t9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))