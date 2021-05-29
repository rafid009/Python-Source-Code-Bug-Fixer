import numpy as np 

def function(x):

	t5 = 2
	z6 = 3
	paths = []
	try:
		if z6 > 4:
			x = z6+t5
			t5 = t5*z6
			t5 = t5*x
			paths.append(1)
		else:
			t5 = 5-x
			t5 = 7*5
			x = x*9
			paths.append(2)
		if t5 <= 9:
			t5 = 8-9
			paths.append(3)
		else:
			z6 = 0/9
			t5 = 7-t5
			x = t5+t5
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		z6 = t5**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))