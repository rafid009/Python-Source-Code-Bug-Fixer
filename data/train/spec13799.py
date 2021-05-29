import numpy as np 

def function(x):

	a4 = x
	t2 = x
	paths = []
	try:
		if x > 1:
			t2 = t2+t2
			a4 = 4+7
			t2 = t2-6
			paths.append(1)
		else:
			x = 2/5
			paths.append(2)
		if a4 < 4:
			t2 = 9*a4
			paths.append(3)
		else:
			t2 = t2+9
			t2 = t2+7
			t2 = 9/5
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		t2 = a4**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))