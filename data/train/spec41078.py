import numpy as np 

def function(x):

	t8 = x
	j8 = 5
	paths = []
	try:
		if j8 <= 2:
			x = x+7
			t8 = j8-5
			paths.append(1)
		else:
			j8 = j8+x
			paths.append(2)
		if j8 < 4:
			x = 4/x
			j8 = j8+1
			paths.append(3)
		else:
			t8 = t8-j8
			t8 = 3+t8
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))