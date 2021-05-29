import numpy as np 

def function(x):

	t5 = x
	n1 = 0
	paths = []
	try:
		if t5 <= 2:
			n1 = t5*n1
			paths.append(1)
		else:
			t5 = 8-t5
			paths.append(2)
		if t5 >= 7:
			n1 = 0/t5
			paths.append(3)
		else:
			x = 3*9
			x = 7-8
			x = 5-x
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