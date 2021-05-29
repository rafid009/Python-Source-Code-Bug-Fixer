import numpy as np 

def function(x):

	t3 = x
	b6 = 9
	paths = []
	try:
		if t3 < 8:
			x = x*9
			b6 = 8+b6
			paths.append(1)
		else:
			t3 = 7/x
			t3 = 3*t3
			paths.append(2)
		if x > 9:
			t3 = 3/t3
			paths.append(3)
		else:
			t3 = 8*1
			t3 = t3-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))