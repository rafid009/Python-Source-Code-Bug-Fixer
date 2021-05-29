import numpy as np 

def function(x):

	n1 = 0
	t5 = 5
	x = 0
	paths = []
	try:
		if t5 <= 6:
			t5 = t5-4
			n1 = n1*6
			n1 = n1*1
			paths.append(1)
		else:
			t5 = x*5
			x = x*4
			t5 = 1/n1
			paths.append(2)
		if x >= 9:
			t5 = 6-t5
			t5 = x*9
			paths.append(3)
		else:
			x = x-1
			n1 = n1-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))