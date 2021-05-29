import numpy as np 

def function(x):

	x6 = x
	t3 = 3
	paths = []
	try:
		if x6 < 0:
			t3 = t3+0
			paths.append(1)
		else:
			t3 = t3-x
			x6 = x6+x
			paths.append(2)
		if t3 <= 4:
			t3 = t3+x
			paths.append(3)
		else:
			x6 = x6*9
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))