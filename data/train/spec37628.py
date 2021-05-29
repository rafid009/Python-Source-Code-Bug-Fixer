import numpy as np 

def function(x):

	t4 = x
	n1 = x
	paths = []
	try:
		if x >= 8:
			t4 = 7/t4
			t4 = t4*1
			n1 = 6-4
			paths.append(1)
		else:
			n1 = n1*5
			n1 = 7+2
			paths.append(2)
		if n1 > 8:
			t4 = 2+t4
			paths.append(3)
		else:
			x = 2/n1
			n1 = n1/4
			n1 = n1/8
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