import numpy as np 

def function(x):

	j4 = x
	t5 = 4
	paths = []
	try:
		if t5 > 5:
			t5 = t5/1
			x = x+t5
			x = 3*x
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if x <= 4:
			x = x+1
			t5 = j4+t5
			t5 = 3/4
			paths.append(3)
		else:
			x = 2-9
			t5 = 7*9
			j4 = t5+j4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))