import numpy as np 

def function(x):

	t5 = 0
	z3 = 4
	paths = []
	try:
		if t5 > 7:
			x = x*z3
			paths.append(1)
		else:
			t5 = 6+z3
			t5 = t5*x
			t5 = t5+1
			paths.append(2)
		if t5 <= 4:
			t5 = 4*t5
			z3 = z3+x
			paths.append(3)
		else:
			x = 2*x
			z3 = z3*z3
			x = 0*x
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