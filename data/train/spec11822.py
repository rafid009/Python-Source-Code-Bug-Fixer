import numpy as np 

def function(x):

	t2 = x
	q6 = 8
	paths = []
	try:
		if x > 9:
			q6 = x/7
			paths.append(1)
		else:
			t2 = t2-6
			t2 = 6+t2
			x = x*8
			paths.append(2)
		if x >= 6:
			x = x*t2
			t2 = 9*t2
			q6 = q6-5
			paths.append(3)
		else:
			t2 = x-t2
			x = x-7
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		t2 = q6**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))