import numpy as np 

def function(x):

	q5 = 5
	t0 = x
	paths = []
	try:
		if q5 < 4:
			x = x+9
			x = x-x
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if t0 <= 6:
			t0 = t0+q5
			x = x-6
			q5 = q5-x
			paths.append(3)
		else:
			t0 = q5-5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		t0 = q5**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))