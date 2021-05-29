import numpy as np 

def function(x):

	t5 = x
	q1 = 5
	paths = []
	try:
		if x < 8:
			q1 = 2*t5
			q1 = 8+x
			paths.append(1)
		else:
			x = 6*x
			x = x-4
			t5 = t5*x
			paths.append(2)
		if q1 <= 3:
			x = q1*3
			paths.append(3)
		else:
			t5 = q1+8
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		t5 = q1**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))