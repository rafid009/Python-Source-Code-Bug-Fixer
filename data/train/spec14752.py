import numpy as np 

def function(x):

	t5 = 0
	n8 = 9
	paths = []
	try:
		if n8 < 0:
			t5 = 4-t5
			x = x-8
			paths.append(1)
		else:
			t5 = t5-x
			x = 2-x
			paths.append(2)
		if n8 <= 2:
			n8 = x-n8
			paths.append(3)
		else:
			x = 5*x
			t5 = 8/t5
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		t5 = t5**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))