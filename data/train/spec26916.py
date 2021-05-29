import numpy as np 

def function(x):

	z9 = 4
	t2 = x
	paths = []
	try:
		if t2 >= 7:
			z9 = 8*z9
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if x > 3:
			z9 = 1+z9
			paths.append(3)
		else:
			t2 = 2*8
			z9 = t2+8
			t2 = x/t2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		t2 = t2**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))