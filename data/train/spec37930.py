import numpy as np 

def function(x):

	a5 = x
	t5 = 6
	paths = []
	try:
		if a5 < 4:
			x = x+a5
			paths.append(1)
		else:
			x = t5*a5
			paths.append(2)
		if a5 <= 4:
			t5 = t5*x
			a5 = 4*a5
			x = x/8
			paths.append(3)
		else:
			x = x-8
			t5 = t5+t5
			a5 = a5*5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		t5 = a5**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))