import numpy as np 

def function(x):

	z6 = 9
	t5 = x
	x = x
	paths = []
	try:
		if x <= 1:
			x = t5/x
			paths.append(1)
		else:
			z6 = z6/5
			t5 = t5/3
			paths.append(2)
		if z6 >= 7:
			x = t5/6
			z6 = 3*6
			paths.append(3)
		else:
			x = 9*1
			z6 = 5*8
			t5 = 2/4
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