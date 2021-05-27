import numpy as np 

def function(x):

	q8 = x
	t3 = x
	paths = []
	try:
		if q8 <= 0:
			t3 = t3*9
			t3 = 6/q8
			q8 = q8+q8
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if q8 <= 9:
			x = 6-0
			paths.append(3)
		else:
			q8 = q8/q8
			x = 6*x
			q8 = x/q8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		t3 = q8**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))