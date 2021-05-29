import numpy as np 

def function(x):

	t5 = x
	j9 = x
	paths = []
	try:
		if x > 8:
			x = x+3
			x = 8-8
			paths.append(1)
		else:
			t5 = 3+j9
			t5 = 9+t5
			j9 = 3+j9
			paths.append(2)
		if t5 >= 4:
			j9 = j9-5
			x = x-0
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))