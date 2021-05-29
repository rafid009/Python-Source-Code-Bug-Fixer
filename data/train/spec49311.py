import numpy as np 

def function(x):

	t5 = 8
	t3 = 1
	paths = []
	try:
		if x < 1:
			t5 = 6/x
			t5 = t5+6
			paths.append(1)
		else:
			x = t3*t5
			paths.append(2)
		if x > 7:
			t3 = t3-x
			t5 = x+9
			paths.append(3)
		else:
			t3 = t3*3
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		t3 = t5**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))