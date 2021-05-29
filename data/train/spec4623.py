import numpy as np 

def function(x):

	t4 = 4
	f3 = 4
	paths = []
	try:
		if t4 < 6:
			t4 = 7*8
			f3 = x-6
			paths.append(1)
		else:
			t4 = t4-2
			paths.append(2)
		if x > 9:
			t4 = t4-8
			t4 = t4/5
			paths.append(3)
		else:
			x = x/6
			f3 = f3*f3
			t4 = t4/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))