import numpy as np 

def function(x):

	t3 = x
	z4 = x
	paths = []
	try:
		if x > 8:
			t3 = t3/3
			x = x*x
			z4 = x+2
			paths.append(1)
		else:
			t3 = t3*2
			t3 = t3+9
			x = 4+x
			paths.append(2)
		if x > 1:
			t3 = t3+z4
			x = 0/5
			z4 = 8*0
			paths.append(3)
		else:
			z4 = t3/x
			x = x*2
			z4 = 6*z4
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