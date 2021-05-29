import numpy as np 

def function(x):

	j4 = x
	t8 = x
	paths = []
	try:
		if x > 1:
			x = 0*x
			t8 = j4/4
			paths.append(1)
		else:
			x = x*4
			t8 = 5*t8
			t8 = x+5
			paths.append(2)
		if x <= 3:
			t8 = x+3
			x = 0-3
			paths.append(3)
		else:
			j4 = 9*7
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		t8 = t8**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))