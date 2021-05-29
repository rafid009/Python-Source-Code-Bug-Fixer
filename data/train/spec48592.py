import numpy as np 

def function(x):

	t5 = 6
	j4 = 9
	paths = []
	try:
		if x <= 7:
			x = x+x
			paths.append(1)
		else:
			x = x+j4
			paths.append(2)
		if t5 <= 3:
			x = x+9
			paths.append(3)
		else:
			t5 = 4+t5
			j4 = j4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))