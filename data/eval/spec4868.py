import numpy as np 

def function(x):

	t3 = x
	a7 = x
	paths = []
	try:
		if x > 3:
			t3 = t3*1
			x = 6/x
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if t3 >= 5:
			x = x/a7
			a7 = a7+5
			t3 = 0-4
			paths.append(3)
		else:
			t3 = t3*t3
			a7 = a7-6
			x = x-7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		t3 = a7**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))