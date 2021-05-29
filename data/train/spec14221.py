import numpy as np 

def function(x):

	q2 = x
	t5 = 8
	paths = []
	try:
		if q2 <= 8:
			t5 = q2-t5
			t5 = t5+7
			x = x-5
			paths.append(1)
		else:
			q2 = q2*q2
			t5 = t5/x
			paths.append(2)
		if q2 <= 4:
			q2 = 9/x
			paths.append(3)
		else:
			t5 = 0*q2
			t5 = 1+t5
			x = x/6
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		t5 = q2**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))